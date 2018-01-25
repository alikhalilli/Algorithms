# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 16:45:00 2018

@author: AKhalilli
"""
from databaseAPI import database
from AirAPI import ucip
import xlsxwriter as xls


ucip_conn = ucip('akhalilli', '123456', '193.15.15.131')
workbook = xls.Workbook('report02.xlsx')
bold = workbook.add_format({'bold': True})

##############################################################################
## Segmented DVT
## There is PAM (11 12 6) but offer not exists
##############################################################################
onsubs_query = """SELECT account_id
   FROM subdealer.sdp_dmp_pam pamdmp
  where pamdmp.pam_class_id = 12
    and pamdmp.account_id not in
        (select offerdmp.account_id
           from subdealer.sdp_dmp_offer offerdmp
          where offerdmp.offer_id in ('114', '115', '116', '117'))"""
onsubsDB = database('onsubs')
cursor = onsubsDB.executeCursor(onsubs_query)

worksheet = workbook.add_worksheet('Segmented(There is no offer)')
worksheet.write('A1', 'MSISDN', bold)
worksheet.write('B1', 'OfferID', bold)
worksheet.write('C1', 'Start Date', bold)
worksheet.write('D1', 'Expire Date', bold)
row, col = 1, 0

for msisdn in cursor:
    msisdn = ''.join(msisdn)
    acc_details = ucip_conn.GetAccountDetails(msisdn)
    off_details = ucip_conn.GetOffers(msisdn)
    if ((ucip_conn.searchValue("offerID", "112", acc_details) == None and 
        ucip_conn.searchValue("offerID", "114", acc_details) == None and 
        ucip_conn.searchValue("offerID", "115", acc_details) == None and 
        ucip_conn.searchValue("offerID", "116", acc_details) == None and
        ucip_conn.searchValue("offerID", "117", acc_details) == None) and 
        ucip_conn.searchValue("pamClassID", "12", acc_details) != None):
        worksheet.write(row, col, msisdn)
        if 'offerInformation' in off_details:
            for offerinfo in off_details['offerInformation']:
                worksheet.write(row, col + 1, offerinfo['offerID'])
                worksheet.write(row, col + 2, offerinfo['startDate'])
                worksheet.write(row, col + 3, offerinfo['expiryDate'])
                row += 1
        else:
            row += 1
#workbook.close()
onsubsDB.close()



##############################################################################
## Region DVT
## There is offer 103, but not PAM (11 11 6)
##############################################################################

onsubs_query = """SELECT offerdmp.account_id
  FROM subdealer.sdp_dmp_offer offerdmp
 WHERE offerdmp.offer_id = '103'
   AND offerdmp.account_id NOT IN
       (SELECT pamdmp.account_id
          FROM subdealer.sdp_dmp_pam pamdmp
         WHERE pamdmp.pam_class_id = '11'
           AND pamdmp.pam_service_id = '11'
           AND pamdmp.schedule_id = '6')"""
onsubsDB = database('onsubs')
cursor = onsubsDB.executeCursor(onsubs_query)
msisdns = []
for msisdn in cursor:
    msisdns.extend(msisdn)
onsubsDB.close()


airdr_query = """SELECT pm.subscribernumber
  FROM pam_record partition(p20170711) pm
 WHERE pm.pameventtype = 'pamDelete'
   AND pm.pamserviceid = '11'
   AND pm.pamclassid = '11'
   AND pm.subscribernumber IN
       (SELECT ad.subscribernumber
          FROM adjustment_cs3 partition(p20170711) ad
         WHERE ad.newserviceclass IN ('44', '80'))
   AND pm.subscribernumber IN (SELECT oa.subscribernumber
                                 FROM operation.adjustment_cs4_oa partition(p20170711) oa
                                WHERE oa.offerid = 103
                                GROUP BY oa.subscribernumber, oa.offerid
                               HAVING count(1) = 1)
"""
airdrDB = database('airdr')
cursor = airdrDB.executeCursor(airdr_query)
for msisdn in cursor:
    msisdns.extend(msisdn)
airdrDB.close()


worksheet = workbook.add_worksheet('Region DVT - there is no PAM')
worksheet.write('A1', 'MSISDN', bold)
worksheet.write('B1', 'OfferID', bold)
worksheet.write('C1', 'Start Date', bold)
worksheet.write('D1', 'Expire Date', bold)

row, col = 1, 0

for msisdn in msisdns:
    acc_details = ucip_conn.GetAccountDetails(msisdn)
    off_details = ucip_conn.GetOffers(msisdn)
    if ucip_conn.searchValue("offerID", "103", acc_details) != None and ucip_conn.searchValue("pamClassID", "11", acc_details) == None:
        worksheet.write(row, col, msisdn)
        for offerinfo in off_details['offerInformation']:
            worksheet.write(row, col + 1, offerinfo['offerID'])
            worksheet.write(row, col + 2, offerinfo['startDate'])
            worksheet.write(row, col + 3, offerinfo['expiryDate'])
            row += 1
#workbook.close()

##############################################################################
## Region DVT
## There is offer PAM 11 11 6, but not offer 103
##############################################################################
onsubs_query = """SELECT account_id
   FROM subdealer.sdp_dmp_pam pamdmp
  where pamdmp.pam_class_id = 11
    and pamdmp.account_id not in
        (select offerdmp.account_id
           from subdealer.sdp_dmp_offer offerdmp
          where offerdmp.offer_id in ('103'))"""
onsubsDB = database('onsubs')
cursor = onsubsDB.executeCursor(onsubs_query)

worksheet = workbook.add_worksheet('Region DVT - there is no offer')
worksheet.write('A1', 'MSISDN', bold)
worksheet.write('B1', 'OfferID', bold)
worksheet.write('C1', 'Start Date', bold)
worksheet.write('D1', 'Expire Date', bold)

row, col = 1, 0

for msisdn in cursor:
    msisdn = ''.join(msisdn)
    acc_details = ucip_conn.GetAccountDetails(msisdn)
    off_details = ucip_conn.GetOffers(msisdn)
    if ucip_conn.searchValue("offerID", "103", acc_details) == None and ucip_conn.searchValue("pamClassID", "11", acc_details) != None:
        worksheet.write(row, col, msisdn)
        if 'offerInformation' in off_details:
            for offerinfo in off_details['offerInformation']:
                worksheet.write(row, col + 1, offerinfo['offerID'])
                worksheet.write(row, col + 2, offerinfo['startDate'])
                worksheet.write(row, col + 3, offerinfo['expiryDate'])
                row += 1
        else:
            row += 1
onsubsDB.close()
workbook.close()
