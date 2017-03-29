rem python gitinspector.py -HlmrTw --until=2016/09/01 ssh://git@stash.billing.ru:2222/m2mcc/m2m_cc_gui.git
REM python gitinspector.py --until=2016/09/01 ssh://git@stash.billing.ru:2222/m2mcc/m2m_cc_gui.git >> out.txt
REM python gitinspector.py ssh://git@stash.billing.ru:2222/scc_cp/sc_cp_apps.git
REm python gitinspector.py ssh://git@stash.billing.ru:2222/crm_cis/cis_engine.git >> out.txt
python gitinspector.py --since=2016/09/01 ssh://git@stash.billing.ru:2222/scc_cp/sc_cp_apps.git >> out1.txt
REM python gitinspector.py --format=excel --since=2016/09/01 ssh://git@stash.billing.ru:2222/crm_cis/SBMS_CIS_GROUP_OPS_DOCPART.git ssh://git@stash.billing.ru:2222/crm_cis/SBMS_CIS_OPERATOR.git ssh://git@stash.billing.ru:2222/crm_cis/SBMS_CIS_OPERATOR_DOCPART.git ssh://git@stash.billing.ru:2222/crm_cis/SCR_CIS.git ssh://git@stash.billing.ru:2222/crm_cis/SCR_CIS.SCHEMA.git ssh://git@stash.billing.ru:2222/crm_cis/SCR_CIS.SCHEMA_DOCPART.git ssh://git@stash.billing.ru:2222/crm_cis/SCR_CIS_DOCPART.git