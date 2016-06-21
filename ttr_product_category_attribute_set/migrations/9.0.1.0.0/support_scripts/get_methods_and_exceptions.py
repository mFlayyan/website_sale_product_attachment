# -*- encoding: utf-8 -*-         
from magento import MagentoAPI
import json


#GET PASSWORD AND USERNAME FROM TTDB,
#insert website location without https:// and without xmlrpc path
#insert port 80

magento = MagentoAPI(
   'www.airtools-online.nl', '80', 
   '', ''
)
json_description_of_resources = magento.resources()
json_description_of_possible_global_exceptions = magento.global_faults()
json_description_of_possible_resource_exceptions = magento.resource_faults("sales_order")

print('RESOURCES\n')
print('---------------------------------------\n')
print(json.dumps(
    json_description_of_resources, 
    sort_keys=True, indent=4, separators=(',', ': ')
    )
)
print('---------------------------------------\n')
print('GLOBAL EXCEPTIONS\n')
print(json.dumps(
    json_description_of_possible_global_exceptions, 
    sort_keys=True, indent=4, separators=(',', ': ')
    )
)
print('---------------------------------------\n')
print('RESOURCE EXCEPTIONS\n')
print(json.dumps(
    json_description_of_possible_resource_exceptions, 
    sort_keys=True, indent=4, separators=(',', ': ')
    )
)




