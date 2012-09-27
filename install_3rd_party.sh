#!/bin/sh
if [ ! -d "$HOME/3rd_party_modules_6.0" ]; then
    mkdir "$HOME/3rd_party_modules_6.0"
else
    cd "$HOME/3rd_party_modules_6.0"
    rm ./*
fi
ln -s $HOME/bzr/banking-addons/account_banking $HOME/3rd_party_modules_6.0/account_banking
ln -s $HOME/bzr/banking-addons/account_banking_nl_clieop $HOME/3rd_party_modules_6.0/account_banking_nl_clieop
ln -s $HOME/bzr/banking-addons/account_banking_nl_abnamro $HOME/3rd_party_modules_6.0/account_banking_nl_abnamro
ln -s $HOME/bzr/banking-addons/account_banking_nl_ing $HOME/3rd_party_modules_6.0/account_banking_nl_ing
ln -s $HOME/bzr/extra-6.0/base_external_referentials $HOME/3rd_party_modules_6.0/base_external_referentials
ln -s $HOME/custom-addons/base_report_xlwt $HOME/3rd_party_modules_6.0/base_report_xlwt
ln -s $HOME/bzr/extra-6.0/base_sale_multichannels $HOME/3rd_party_modules_6.0/base_sale_multichannels
ln -s $HOME/bzr/magentoerpconnect-6.0/magentoerpconnect $HOME/3rd_party_modules_6.0/magentoerpconnect
ln -s $HOME/bzr/extra-6.0/product_images_olbs $HOME/3rd_party_modules_6.0/product_images_olbs
ln -s $HOME/bzr/extra-6.0/product_links  $HOME/3rd_party_modules_6.0/product_links 
ln -s $HOME/bzr/extra-6.0/product_m2mcategories  $HOME/3rd_party_modules_6.0/product_m2mcategories 
ln -s $HOME/bzr/therp-addons/trp_update_tax  $HOME/3rd_party_modules_6.0/trp_update_tax

# Hieronder ook een aantal modules, omdat anders de web 6.0 client niet vooruit te branden is
# zorg ervoor dat de akretion addons-no-fluff is geïnstalleerd:
# bzr branch lp:~akretion-team/+junk/addons-no-fluff
ln -s $HOME/bzr/addons-no-fluff/account_no_dashboard $HOME/3rd_party_modules_6.0/account_no_dashboard
ln -s $HOME/bzr/addons-no-fluff/admin_no_dashboard $HOME/3rd_party_modules_6.0/admin_no_dashboard
ln -s $HOME/bzr/addons-no-fluff/purchase_no_dashboard $HOME/3rd_party_modules_6.0/purchase_no_dashboard
ln -s $HOME/bzr/addons-no-fluff/sale_no_dashboard $HOME/3rd_party_modules_6.0/sale_no_dashboard
ln -s $HOME/bzr/addons-no-fluff/stock_no_dashboard $HOME/3rd_party_modules_6.0/stock_no_dashboard

exit 0