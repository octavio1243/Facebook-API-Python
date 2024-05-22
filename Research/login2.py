import requests

burp0_url = "https://b-graph.facebook.com:443/graphql"
burp0_headers = {
    "X-Fb-Ta-Logging-Ids": "graphql:67427f8e-442c-4467-a6ec-68cf725a30c5", 
    "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "X-Graphql-Request-Purpose": "fetch", 
    "X-Fb-Background-State": "1", 
    "X-Fb-Sim-Hni": "722310", 
    "X-Fb-Net-Hni": "722310", 
    "X-Fb-Request-Analytics-Tags": "{\"network_tags\":{\"product\":\"350685531728\",\"purpose\":\"fetch\",\"request_category\":\"graphql\",\"retry_attempt\":\"0\"},\"application_tags\":\"graphservice\"}", 
    "X-Graphql-Client-Library": "graphservice", 
    "X-Fb-Friendly-Name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request", 
    "X-Fb-Privacy-Context": "3643298472347298", 
    "User-Agent": "[FBAN/FB4A;FBAV/443.0.0.23.229;FBBV/543547945;FBDM/{density=3.5,width=1440,height=2759};FBLC/es_LA;FBRV/0;FBCR/Claro AR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N975F;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]", 
    "X-Fb-Connection-Type": "WIFI", 
    "X-Fb-Device-Group": "4532", 
    "X-Tigon-Is-Retry": "False", 
    "Accept-Encoding": "gzip, deflate, br", 
    "X-Fb-Http-Engine": "Liger", 
    "X-Fb-Client-Ip": "True", 
    "X-Fb-Server-Cluster": "True"
}
burp0_data = {
    "method": "post", 
    "pretty": "false", 
    "format": "json", 
    "server_timestamps": "true", 
    "locale": "es_LA", 
    "purpose": "fetch", 
    "fb_api_req_friendly_name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request", 
    "fb_api_caller_class": "graphservice", 
    "client_doc_id": "11994080424240083948543644217", 
    "variables": "{\"params\":{\"params\":\"{\\\"params\\\":\\\"{\\\\\\\"client_input_params\\\\\\\":{\\\\\\\"sim_phones\\\\\\\":[],\\\\\\\"secure_family_device_id\\\\\\\":\\\\\\\"b7f32c35-acf8-4cbe-be40-f75d8a596f5c\\\\\\\",\\\\\\\"attestation_result\\\\\\\":{\\\\\\\"keyHash\\\\\\\":\\\\\\\"9bd4c44ee9638efa6f539b9e6e4b39813746dcf0e52de14120f0464560a0620f\\\\\\\",\\\\\\\"signature\\\\\\\":\\\\\\\"MEUCIQCXgRE41kDKy67CqSiG6ZiwxmgJ3rmkJ4qQkvQtNJfJoAIgAK1lxbqmH6qGnp31fJt5myPkQlBChoWr8qItNwY1zK4=\\\\\\\",\\\\\\\"data\\\\\\\":\\\\\\\"dXNlcm5hbWU6ZXhhbXBsZUB0ZXN0LmNvbXxjaGFsbGVuZ2Vfbm9uY2U6QmhjYXdkcnltMHVzWFJJL2dibkxJNXlMUndxbUtXSFZEcTZ0RWEyMVgzND18\\\\\\\"},\\\\\\\"auth_secure_device_id\\\\\\\":\\\\\\\"\\\\\\\",\\\\\\\"has_whatsapp_installed\\\\\\\":1,\\\\\\\"password\\\\\\\":\\\\\\\"#PWD_FB4A:2:1716392126:ARiWpMaN7rWmMbqYOQ8AAXRdBwTaJunrgYpy3+Xd28tGPf0EVcPp+8e\\\\/6W7IC81Q8p+daKWLH45B4y01E6oJ+eRfVak8\\\\/TCTcKaz7EekizTSNdWVIvAl5bTIfHrftVoppCZ\\\\/43kueNXTGeVuuKn8S2t5WHDRQc8c11Qvjp2dpdwdwoTYlg\\\\/OBIQuT\\\\/XQJjGQLExA8\\\\/s9cAVWKetIJYfO6rqYxFunK3gapidsFeT1Ros26fIE7R33y0nQWe0dN1i\\\\/FigzTKlpiA1upg3w7cnEr7cMyLL2pA\\\\/5LAX3JqRFqagny2ti4p3ABBTKAo5sRFYc3UBLVEYhGL6PU1rF5y1A9Vpr8HIeC2LLs66GZSCk3JazxuN3tKulc7MZ4CbDipfXoux++DKaQtw=\\\\\\\",\\\\\\\"sso_token_map_json_string\\\\\\\":\\\\\\\"\\\\\\\",\\\\\\\"event_flow\\\\\\\":\\\\\\\"login_manual\\\\\\\",\\\\\\\"sim_serials\\\\\\\":[],\\\\\\\"client_known_key_hash\\\\\\\":\\\\\\\"9bd4c44ee9638efa6f539b9e6e4b39813746dcf0e52de14120f0464560a0620f36235a0498ef80c680baec91457278e20547a74c5387fa876a8efb6e3fb027d5\\\\\\\",\\\\\\\"encrypted_msisdn\\\\\\\":\\\\\\\"\\\\\\\",\\\\\\\"should_show_nested_nta_from_aymh\\\\\\\":0,\\\\\\\"device_id\\\\\\\":\\\\\\\"5413bd64-0cd9-4de6-bb4a-a234d87d62a8\\\\\\\",\\\\\\\"login_attempt_count\\\\\\\":1,\\\\\\\"machine_id\\\\\\\":\\\\\\\"\\\\\\\",\\\\\\\"flash_call_permission_status\\\\\\\":{\\\\\\\"READ_PHONE_STATE\\\\\\\":\\\\\\\"DENIED\\\\\\\",\\\\\\\"READ_CALL_LOG\\\\\\\":\\\\\\\"DENIED\\\\\\\",\\\\\\\"ANSWER_PHONE_CALLS\\\\\\\":\\\\\\\"DENIED\\\\\\\"},\\\\\\\"accounts_list\\\\\\\":[],\\\\\\\"family_device_id\\\\\\\":\\\\\\\"5413bd64-0cd9-4de6-bb4a-a234d87d62a8\\\\\\\",\\\\\\\"fb_ig_device_id\\\\\\\":[],\\\\\\\"device_emails\\\\\\\":[],\\\\\\\"try_num\\\\\\\":2,\\\\\\\"lois_settings\\\\\\\":{\\\\\\\"lois_token\\\\\\\":\\\\\\\"\\\\\\\",\\\\\\\"lara_override\\\\\\\":\\\\\\\"\\\\\\\"},\\\\\\\"event_step\\\\\\\":\\\\\\\"home_page\\\\\\\",\\\\\\\"headers_infra_flow_id\\\\\\\":\\\\\\\"\\\\\\\",\\\\\\\"openid_tokens\\\\\\\":{},\\\\\\\"contact_point\\\\\\\":\\\\\\\"example@test.com\\\\\\\"},\\\\\\\"server_params\\\\\\\":{\\\\\\\"should_trigger_override_login_2fa_action\\\\\\\":0,\\\\\\\"is_from_logged_out\\\\\\\":0,\\\\\\\"should_trigger_override_login_success_action\\\\\\\":0,\\\\\\\"login_credential_type\\\\\\\":\\\\\\\"none\\\\\\\",\\\\\\\"server_login_source\\\\\\\":\\\\\\\"login\\\\\\\",\\\\\\\"waterfall_id\\\\\\\":\\\\\\\"670a3155-c32c-4f04-b4ab-78cc3f19a742\\\\\\\",\\\\\\\"login_source\\\\\\\":\\\\\\\"Login\\\\\\\",\\\\\\\"is_platform_login\\\\\\\":0,\\\\\\\"pw_encryption_try_count\\\\\\\":1,\\\\\\\"INTERNAL__latency_qpl_marker_id\\\\\\\":36707139,\\\\\\\"offline_experiment_group\\\\\\\":\\\\\\\"caa_iteration_v6_perf_fb_2\\\\\\\",\\\\\\\"is_from_landing_page\\\\\\\":0,\\\\\\\"password_text_input_id\\\\\\\":\\\\\\\"zie7ny:91\\\\\\\",\\\\\\\"ar_event_source\\\\\\\":\\\\\\\"login_home_page\\\\\\\",\\\\\\\"username_text_input_id\\\\\\\":\\\\\\\"zie7ny:90\\\\\\\",\\\\\\\"layered_homepage_experiment_group\\\\\\\":null,\\\\\\\"device_id\\\\\\\":\\\\\\\"5413bd64-0cd9-4de6-bb4a-a234d87d62a8\\\\\\\",\\\\\\\"INTERNAL__latency_qpl_instance_id\\\\\\\":2.14721236600667E14,\\\\\\\"reg_flow_source\\\\\\\":\\\\\\\"login_home_native_integration_point\\\\\\\",\\\\\\\"is_caa_perf_enabled\\\\\\\":1,\\\\\\\"credential_type\\\\\\\":\\\\\\\"password\\\\\\\",\\\\\\\"caller\\\\\\\":\\\\\\\"gslr\\\\\\\",\\\\\\\"family_device_id\\\\\\\":\\\\\\\"5413bd64-0cd9-4de6-bb4a-a234d87d62a8\\\\\\\",\\\\\\\"INTERNAL_INFRA_THEME\\\\\\\":\\\\\\\"harm_f\\\\\\\",\\\\\\\"is_from_logged_in_switcher\\\\\\\":0}}\\\"}\",\"bloks_versioning_id\":\"c459b951c037ad3fbe67f94342f309a73154e66c326b3cd823682078d9eeb722\",\"app_id\":\"com.bloks.www.bloks.caa.login.async.send_login_request\"},\"scale\":\"4\",\"nt_context\":{\"using_white_navbar\":true,\"pixel_ratio\":4,\"is_push_on\":true,\"styles_id\":\"196702b4d5dfb9dbf1ded6d58ee42767\",\"bloks_version\":\"c459b951c037ad3fbe67f94342f309a73154e66c326b3cd823682078d9eeb722\"}}", 
    "fb_api_analytics_tags": "[\"GraphServices\"]", 
    "client_trace_id": "67427f8e-442c-4467-a6ec-68cf725a30c5"}
requests.post(burp0_url, headers=burp0_headers, data=burp0_data)