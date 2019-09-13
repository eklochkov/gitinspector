rem python gitinspector.py -HlmrTw --until=2016/09/01 ssh://git@stash.[domain]:2222/m2mcc/m2m_cc_gui.git
REM python gitinspector.py --until=2016/09/01 ssh://git@stash.[domain]:2222/m2mcc/m2m_cc_gui.git >> out.txt
REM python gitinspector.py ssh://git@stash.[domain]:2222/scc_cp/sc_cp_apps.git
REm python gitinspector.py ssh://git@stash.[domain]:2222/crm_cis/cis_engine.git >> out.txt
REM python gitinspector.py --since=2016/09/01 ssh://git@stash.[domain]:2222/scm/uniblp/uniblp.git >> out1.txt
REM python gitinspector.py --since=2017/03/03 --until=2017/03/03 https://[name]@stash.[domain]/scm/spp/spp-ui.git >> out.txt

REM python gitinspector.py --format=excel --since=2016/09/01 ssh://git@stash.[domain]:2222/crm_cis/SBMS_CIS_GROUP_OPS_DOCPART.git ssh://git@stash.billing.ru:2222/crm_cis/SBMS_CIS_OPERATOR.git ssh://git@stash.billing.ru:2222/crm_cis/SBMS_CIS_OPERATOR_DOCPART.git ssh://git@stash.billing.ru:2222/crm_cis/SCR_CIS.git ssh://git@stash.billing.ru:2222/crm_cis/SCR_CIS.SCHEMA.git ssh://git@stash.billing.ru:2222/crm_cis/SCR_CIS.SCHEMA_DOCPART.git ssh://git@stash.billing.ru:2222/crm_cis/SCR_CIS_DOCPART.git

REM ---
REM CHDB DEV
REM python gitinspector.py --since=2017/01/01 https://[name]@stash.[domain]/scm/chargesdb/chargesdb_tests.git https://user_name@stash.domain.com/scm/chargesdb/charging_data_conveyer.git https://user_name@stash.domain.com/scm/chargesdb/customer_guardian.git https://user_name@stash.domain.com/scm/chargesdb/customer_reporter.git https://[name]@stash.[domain]/scm/chargesdb/oapi_chargesdb_api_backend.git >> out.txt

REM for PyCharm --format=excel --since=2018/05/01 --commits --project=PROJECT --repository_name=REP_NAME --login=user_name --password=xxxx
