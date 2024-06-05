import requests

burp0_url = "https://b-graph.facebook.com:443/graphql"
burp0_headers = {"X-Fb-Ta-Logging-Ids": "graphql:8a582ee7-1050-405e-af7c-039081a1064c", "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32", "Content-Type": "application/x-www-form-urlencoded", "X-Graphql-Request-Purpose": "fetch", "X-Fb-Background-State": "1", "X-Fb-Sim-Hni": "722310", "X-Fb-Net-Hni": "722310", "X-Fb-Request-Analytics-Tags": "{\"network_tags\":{\"product\":\"350685531728\",\"purpose\":\"fetch\",\"request_category\":\"graphql\",\"retry_attempt\":\"0\"},\"application_tags\":\"graphservice\"}", "X-Graphql-Client-Library": "graphservice", "X-Fb-Friendly-Name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request", "X-Fb-Privacy-Context": "3643298472347298", "User-Agent": "[FBAN/FB4A;FBAV/443.0.0.23.229;FBBV/543547945;FBDM/{density=3.5,width=1440,height=2759};FBLC/es_LA;FBRV/0;FBCR/Claro AR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N975F;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]", "X-Fb-Connection-Type": "WIFI", "X-Fb-Device-Group": "2768", "X-Tigon-Is-Retry": "False", "Accept-Encoding": "gzip, deflate, br", "X-Fb-Http-Engine": "Liger", "X-Fb-Client-Ip": "True", "X-Fb-Server-Cluster": "True"}
burp0_data = {"method": "post", "pretty": "false", "format": "json", "server_timestamps": "true", "locale": "es_LA", "purpose": "fetch", "fb_api_req_friendly_name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request", "fb_api_caller_class": "graphservice", "client_doc_id": "11994080424240083948543644217", "variables": "{\"params\":{\"params\":\"{\\\"params\\\":\\\"{\\\\\\\"client_input_params\\\\\\\":{\\\\\\\"sim_phones\\\\\\\":[],\\\\\\\"secure_family_device_id\\\\\\\":\\\\\\\"b43d7ce2-17cf-48e6-9557-2767445f28db\\\\\\\",\\\\\\\"attestation_result\\\\\\\":{\\\\\\\"keyHash\\\\\\\":\\\\\\\"7155627ee754b1ad8aa6e25fdef8c5c310e3f64a4c23ae60f12fd09a412e7bb2\\\\\\\",\\\\\\\"signature\\\\\\\":\\\\\\\"MEUCIHN0k\\\\/+sGBk5mP\\\\/hUo3xEM+aiY2GNISrGKy4FskddQnCAiEAjUsBnlhus86qyACX5J+PpjACk21QJpIvL7Qjk8ess0M=\\\\\\\",\\\\\\\"data\\\\\\\":\\\\\\\"dXNlcm5hbWU6ZmFra3JpbmFAZ21haWwuY29tfGNoYWxsZW5nZV9ub25jZTpZWk9veFlRYnhDblpWcWZaUVFzT09OcFBxdUVIb0RXbkJpTXJmUEUwNmhZPXw=\\\\\\\"},\\\\\\\"auth_secure_device_id\\\\\\\":\\\\\\\"\\\\\\\",\\\\\\\"has_whatsapp_installed\\\\\\\":1,\\\\\\\"password\\\\\\\":\\\\\\\"#PWD_FB4A:2:1716407635:AejzyUFr9xnXek2fQ4EAAU+eiD4KKI7xwfZRlS2Ghhp1bhzJtfneHTijwFHAQAaE9TfryHmLMNWm0P0PhmIL0E58DvY8FDR6HwSAWKNSaHIOKE3sUB6xpASnZgWRNBw\\\\/PxlEphfzxdAFOmOH91h7AwgEL1qJbl2h7DeqfRr57DOUfWFAQeByVSztYpoc4u2HrakUDxyZ0b1NF9wNgu3QT1nf1cS1Gv\\\\/g96biKUNlC2+kZFx0KDJO7UwgVXdPl4sBhrZtihs+OeL6RZmLu1oAz9cg0RyO5l0NoMSNWnPO5a3oh6vEMJVwScGMW2yQhcSwe7wdHdk\\\\/z\\\\/LJVvZs4GQEAfKW8l4eJExqfkr7Yl1Zy1mJes10m5dMchtENLuB9Vcc6SCZlruROEcu\\\\/Q==\\\\\\\",\\\\\\\"sso_token_map_json_string\\\\\\\":\\\\\\\"\\\\\\\",\\\\\\\"event_flow\\\\\\\":\\\\\\\"login_manual\\\\\\\",\\\\\\\"sim_serials\\\\\\\":[],\\\\\\\"client_known_key_hash\\\\\\\":\\\\\\\"f987a06896657696031bc785f711dc63b5465c53ac4e91fa50dfb7dbca30e7c97155627ee754b1ad8aa6e25fdef8c5c310e3f64a4c23ae60f12fd09a412e7bb2\\\\\\\",\\\\\\\"encrypted_msisdn\\\\\\\":\\\\\\\"\\\\\\\",\\\\\\\"should_show_nested_nta_from_aymh\\\\\\\":0,\\\\\\\"device_id\\\\\\\":\\\\\\\"3b3196f0-d0bf-4301-8962-d8db68f38eff\\\\\\\",\\\\\\\"login_attempt_count\\\\\\\":1,\\\\\\\"machine_id\\\\\\\":\\\\\\\"\\\\\\\",\\\\\\\"flash_call_permission_status\\\\\\\":{\\\\\\\"READ_PHONE_STATE\\\\\\\":\\\\\\\"DENIED\\\\\\\",\\\\\\\"READ_CALL_LOG\\\\\\\":\\\\\\\"DENIED\\\\\\\",\\\\\\\"ANSWER_PHONE_CALLS\\\\\\\":\\\\\\\"DENIED\\\\\\\"},\\\\\\\"accounts_list\\\\\\\":[],\\\\\\\"family_device_id\\\\\\\":\\\\\\\"3b3196f0-d0bf-4301-8962-d8db68f38eff\\\\\\\",\\\\\\\"fb_ig_device_id\\\\\\\":[],\\\\\\\"device_emails\\\\\\\":[],\\\\\\\"try_num\\\\\\\":1,\\\\\\\"lois_settings\\\\\\\":{\\\\\\\"lois_token\\\\\\\":\\\\\\\"\\\\\\\",\\\\\\\"lara_override\\\\\\\":\\\\\\\"\\\\\\\"},\\\\\\\"event_step\\\\\\\":\\\\\\\"home_page\\\\\\\",\\\\\\\"headers_infra_flow_id\\\\\\\":\\\\\\\"\\\\\\\",\\\\\\\"openid_tokens\\\\\\\":{},\\\\\\\"contact_point\\\\\\\":\\\\\\\"fakkrina@gmail.com\\\\\\\"},\\\\\\\"server_params\\\\\\\":{\\\\\\\"should_trigger_override_login_2fa_action\\\\\\\":0,\\\\\\\"is_from_logged_out\\\\\\\":0,\\\\\\\"should_trigger_override_login_success_action\\\\\\\":0,\\\\\\\"login_credential_type\\\\\\\":\\\\\\\"none\\\\\\\",\\\\\\\"server_login_source\\\\\\\":\\\\\\\"login\\\\\\\",\\\\\\\"waterfall_id\\\\\\\":\\\\\\\"6b4d97ec-d3e8-4e7a-afe6-8ac6d644f142\\\\\\\",\\\\\\\"login_source\\\\\\\":\\\\\\\"Login\\\\\\\",\\\\\\\"is_platform_login\\\\\\\":0,\\\\\\\"pw_encryption_try_count\\\\\\\":1,\\\\\\\"INTERNAL__latency_qpl_marker_id\\\\\\\":36707139,\\\\\\\"offline_experiment_group\\\\\\\":\\\\\\\"caa_iteration_v6_perf_fb_2\\\\\\\",\\\\\\\"is_from_landing_page\\\\\\\":0,\\\\\\\"password_text_input_id\\\\\\\":\\\\\\\"8s79mj:94\\\\\\\",\\\\\\\"ar_event_source\\\\\\\":\\\\\\\"login_home_page\\\\\\\",\\\\\\\"username_text_input_id\\\\\\\":\\\\\\\"8s79mj:93\\\\\\\",\\\\\\\"layered_homepage_experiment_group\\\\\\\":null,\\\\\\\"device_id\\\\\\\":\\\\\\\"3b3196f0-d0bf-4301-8962-d8db68f38eff\\\\\\\",\\\\\\\"INTERNAL__latency_qpl_instance_id\\\\\\\":5.3109772300667E13,\\\\\\\"reg_flow_source\\\\\\\":\\\\\\\"login_home_native_integration_point\\\\\\\",\\\\\\\"is_caa_perf_enabled\\\\\\\":1,\\\\\\\"credential_type\\\\\\\":\\\\\\\"password\\\\\\\",\\\\\\\"caller\\\\\\\":\\\\\\\"gslr\\\\\\\",\\\\\\\"family_device_id\\\\\\\":\\\\\\\"3b3196f0-d0bf-4301-8962-d8db68f38eff\\\\\\\",\\\\\\\"INTERNAL_INFRA_THEME\\\\\\\":\\\\\\\"harm_f\\\\\\\",\\\\\\\"is_from_logged_in_switcher\\\\\\\":0}}\\\"}\",\"bloks_versioning_id\":\"c459b951c037ad3fbe67f94342f309a73154e66c326b3cd823682078d9eeb722\",\"app_id\":\"com.bloks.www.bloks.caa.login.async.send_login_request\"},\"scale\":\"4\",\"nt_context\":{\"using_white_navbar\":true,\"pixel_ratio\":4,\"is_push_on\":true,\"styles_id\":\"196702b4d5dfb9dbf1ded6d58ee42767\",\"bloks_version\":\"c459b951c037ad3fbe67f94342f309a73154e66c326b3cd823682078d9eeb722\"}}", "fb_api_analytics_tags": "[\"GraphServices\"]", "client_trace_id": "8a582ee7-1050-405e-af7c-039081a1064c"}
requests.post(burp0_url, headers=burp0_headers, data=burp0_data)



"""

HTTP/2 200 OK
Content-Type: text/javascript; charset=UTF-8
X-Fb-Optimizer: 0
Access-Control-Expose-Headers: X-FB-Debug, X-Loader-Length, X-Stack
Access-Control-Allow-Methods: OPTIONS
Access-Control-Allow-Credentials: true
Access-Control-Allow-Origin: https://facebook.com
Vary: Origin
Vary: Accept-Encoding
Facebook-Api-Version: v1.0
Strict-Transport-Security: max-age=15552000; preload
Pragma: no-cache
Cache-Control: private, no-cache, no-store, must-revalidate
Expires: Sat, 01 Jan 2000 00:00:00 GMT
X-Fb-Request-Id: AllamUtBK6OWhX6wtUUpDHT
X-Fb-Trace-Id: Ftx+JFPmz0V
X-Fb-Rev: 1013689444
X-Fb-Debug: f9R5/t/K1bMRFrE4nvBc7PkSZUPtxsGC72Z8dHcjRJz85nXYWH3ycl5ouOOg+2DxNn14OSaqmw1wD0atQpYEIw==
Content-Length: 8847
Date: Wed, 22 May 2024 19:53:56 GMT
X-Fb-Client-Ip-Forwarded: 179.63.242.181
X-Fb-Server-Cluster-Forwarded: eze1c01
X-Fb-Connection-Quality: GOOD; q=0.7, rtt=67, rtx=0, c=10, mss=1392, tbw=67581, tp=-1, tpl=-1, uplat=1486, ullat=0
Alt-Svc: h3=":443"; ma=86400

{"data":{"fb_bloks_action":{"root_action":{"action":{"action_bundle":{"bloks_bundle_action":"{\"layout\":{\"bloks_payload\":{\"data\":[{\"id\":\"iu85jfvhe\",\"type\":\"gs\",\"data\":{\"key\":\"CAA_REQUEST_ATTESTATION:request_challenge_nonce\",\"mode\":\"d\",\"initial\":{}}}],\"props\":[{\"id\":\"-6917714003244327204\",\"name\":\"ttrc_instance_id\"},{\"id\":\"2231046902902521263\",\"name\":\"override_login_success_action\"},{\"id\":\"-3430068907069239942\",\"name\":\"override_login_2fa_action\"}],\"error_attribution\":{\"logging_id\":\"{\\\"callsite\\\":\\\"{\\\\\\\"product\\\\\\\":\\\\\\\"bloks_caa_login\\\\\\\",\\\\\\\"feature\\\\\\\":\\\\\\\"com.bloks.www.bloks.caa.login.async.send_login_request\\\\\\\",\\\\\\\"integration\\\\\\\":\\\\\\\"bloks_screen\\\\\\\",\\\\\\\"oncall\\\\\\\":\\\\\\\"caa_login\\\\\\\"}\\\",\\\"push_phase\\\":\\\"C3\\\",\\\"version\\\":1,\\\"request_id\\\":\\\"AllamUtBK6OWhX6wtUUpDHT\\\",\\\"www_revision\\\":1013689444}\",\"source_map_id\":\"NymEcIqC\"},\"action\":\" (bk.action.core.TakeLast, (bk.action.core.TakeLast, (bk.action.bloks.WriteGlobalConsistencyStore, \\\"CAA_REQUEST_ATTESTATION:request_challenge_nonce\\\", (bk.action.core.Apply, (bk.action.core.FuncConst, (bk.action.map.Merge, (bk.action.core.GetArg, 0), (bk.action.map.Make, (bk.action.array.Make, \\\"com.bloks.www.bloks.caa.login.async.send_login_request\\\"), (bk.action.array.Make, \\\"mDi+bZxN4a+0yEVn72uPHS3rSPnKERVQW\\\\\\\/2TSh3Lj\\\\\\\/c=\\\")))), (bk.action.bloks.GetVariable2, \\\"iu85jfvhe\\\"))), (bk.action.logging.LogEvent, \\\"caa_login_client_events_fb_msgr\\\", \\\"\\\", (bk.action.map.Make, (bk.action.array.Make, \\\"core\\\", \\\"login_params\\\"), (bk.action.array.Make, (bk.action.map.Make, (bk.action.array.Make, \\\"event\\\", \\\"event_category\\\", \\\"event_flow\\\", \\\"event_request_id\\\", \\\"event_step\\\", \\\"is_dark_mode\\\", \\\"exception_code\\\", \\\"exception_message\\\", \\\"exception_type\\\", \\\"extra_client_data\\\", \\\"extra_server_data_encrypted\\\", \\\"extra_client_data_bks_input\\\", \\\"logged_out_identifier\\\", \\\"logged_in_identifier\\\", \\\"waterfall_id\\\", \\\"reduction_push_phase\\\", \\\"reduction_region\\\", \\\"access_flow_version\\\"), (bk.action.array.Make, \\\"login_request_attestation_nonce_validation_succeeded\\\", \\\"attestation\\\", \\\"login\\\", \\\"a8268f7b-80ce-4f60-a453-36b6c6e7880e\\\", \\\"home_page\\\", (fb.action.IsDarkModeEnabled), 0, \\\"\\\", \\\"\\\", (bk.action.map.Make, (bk.action.array.Make, \\\"is_from_switcher\\\", \\\"fblite_client_id\\\", \\\"is_from_logged_out\\\"), (bk.action.array.Make, \\\"0\\\", \\\"\\\", \\\"0\\\")), \\\"ARuAokB81lGvLW0VQKuWKaHjJMisnEAdePeG57vA4w2uZYiEg9Fu5LqyKTce84Z4cesL2Oq2ceL7TQuffL2AvsOHNz522R5mKSVAB6iAORBIEdaLHhZNsSFbvoVXpaeNid4p5Q3Fvq9DlNLg7k7JvXw\\\", (bk.action.map.Make, (bk.action.array.Make), (bk.action.array.Make)), \\\"\\\", \\\"\\\", \\\"6b4d97ec-d3e8-4e7a-afe6-8ac6d644f142\\\", \\\"C3\\\", \\\"altoona\\\", \\\"\\\")), (bk.action.map.Make, (bk.action.array.Make), (bk.action.array.Make)))))), (bk.action.core.TakeLast, (bk.action.qpl.MarkerAnnotate, 2293785, 0, (bk.action.map.Make, (bk.action.array.Make, \\\"login_type\\\", \\\"login_source\\\"), (bk.action.array.Make, \\\"Password\\\", \\\"Login\\\"))), (bk.action.core.TakeLast, (bk.action.qpl.MarkerPoint, 2293785, 0, \\\"success_response\\\", (bk.action.tree.Make, 13747)), 1), (bk.action.caa.SaveSmartlockSecret, (bk.action.core.GetArg, 0), \\\"AXbg1w_9Q5NLNZMCK6nz3TK6Fyd6nDUIHzuqMHYgCyP4U7XpM3wB1hTzRWDaKZXlaTg0rH3Xdh8USLkTTfM9-GruERkW0bUpLijWBur2yeEpW4E2aC49K5P7i_GBHHOCi3moT9KPDGH0\\\"), (bk.action.core.TakeLast, (bk.action.caa.HandleLoginResponse, (bk.action.tree.Make, 15942, 35, \\\"{\\\\\\\"session_key\\\\\\\":\\\\\\\"5.9AFpc7fpDCP1iA.1716407636.50-100023854695779\\\\\\\",\\\\\\\"uid\\\\\\\":100023854695779,\\\\\\\"secret\\\\\\\":\\\\\\\"3607806ea45b85cb3b43188a35628c2f\\\\\\\",\\\\\\\"access_token\\\\\\\":\\\\\\\"EAAAAUaZA8jlABO8nrsYSQeG0ooDZARP72V4KcmtXXdvk4epxpg10X2ZB6P9sEVgDI25EbmR8iZAX6wCUWcHPxjt31GmLZBkZCkI2LH38evZAaZAAlNIyZAAgzLzkktgm9rzxjg1PbTQPD8Iwi34hlUO1JyfooKpRR5ZAKIyCfzteOoJIJtC3De3ipBbfMA3NCwmQLLZAgZDZD\\\\\\\",\\\\\\\"machine_id\\\\\\\":\\\\\\\"U01OZk7-ZuF0BRjY_lLnkX3s\\\\\\\",\\\\\\\"session_cookies\\\\\\\":[{\\\\\\\"name\\\\\\\":\\\\\\\"c_user\\\\\\\",\\\\\\\"value\\\\\\\":\\\\\\\"100023854695779\\\\\\\",\\\\\\\"expires\\\\\\\":\\\\\\\"Thu, 22 May 2025 19:53:55 GMT\\\\\\\",\\\\\\\"expires_timestamp\\\\\\\":1747943635,\\\\\\\"domain\\\\\\\":\\\\\\\".facebook.com\\\\\\\",\\\\\\\"path\\\\\\\":\\\\\\\"\\\\\\\\\\\\\\\/\\\\\\\",\\\\\\\"secure\\\\\\\":true,\\\\\\\"httponly\\\\\\\":null,\\\\\\\"samesite\\\\\\\":\\\\\\\"None\\\\\\\"},{\\\\\\\"name\\\\\\\":\\\\\\\"xs\\\\\\\",\\\\\\\"value\\\\\\\":\\\\\\\"50:9AFpc7fpDCP1iA:2:1716407636:-1:15917\\\\\\\",\\\\\\\"expires\\\\\\\":\\\\\\\"Thu, 22 May 2025 19:53:55 GMT\\\\\\\",\\\\\\\"expires_timestamp\\\\\\\":1747943635,\\\\\\\"domain\\\\\\\":\\\\\\\".facebook.com\\\\\\\",\\\\\\\"path\\\\\\\":\\\\\\\"\\\\\\\\\\\\\\\/\\\\\\\",\\\\\\\"secure\\\\\\\":true,\\\\\\\"httponly\\\\\\\":true,\\\\\\\"samesite\\\\\\\":\\\\\\\"None\\\\\\\"},{\\\\\\\"name\\\\\\\":\\\\\\\"fr\\\\\\\",\\\\\\\"value\\\\\\\":\\\\\\\"0CQtytauc2RjGtykC.AWU7aV3w5XLezlEcqdQXtgix4jo.BmTk1T..AAA.0.0.BmTk1T.AWVXUgvv0Do\\\\\\\",\\\\\\\"expires\\\\\\\":\\\\\\\"Tue, 20 Aug 2024 19:53:55 GMT\\\\\\\",\\\\\\\"expires_timestamp\\\\\\\":1724183635,\\\\\\\"domain\\\\\\\":\\\\\\\".facebook.com\\\\\\\",\\\\\\\"path\\\\\\\":\\\\\\\"\\\\\\\\\\\\\\\/\\\\\\\",\\\\\\\"secure\\\\\\\":true,\\\\\\\"httponly\\\\\\\":true,\\\\\\\"samesite\\\\\\\":\\\\\\\"None\\\\\\\"},{\\\\\\\"name\\\\\\\":\\\\\\\"datr\\\\\\\",\\\\\\\"value\\\\\\\":\\\\\\\"U01OZk7-ZuF0BRjY_lLnkX3s\\\\\\\",\\\\\\\"expires\\\\\\\":\\\\\\\"Thu, 26 Jun 2025 19:53:55 GMT\\\\\\\",\\\\\\\"expires_timestamp\\\\\\\":1750967635,\\\\\\\"domain\\\\\\\":\\\\\\\".facebook.com\\\\\\\",\\\\\\\"path\\\\\\\":\\\\\\\"\\\\\\\\\\\\\\\/\\\\\\\",\\\\\\\"secure\\\\\\\":true,\\\\\\\"httponly\\\\\\\":true,\\\\\\\"samesite\\\\\\\":\\\\\\\"None\\\\\\\"}],\\\\\\\"analytics_claim\\\\\\\":\\\\\\\"hmac.AR3WO8eE72CmFzZwfEojOqVI5RZ-yQh7_YlkFAYZLeboFemC\\\\\\\",\\\\\\\"confirmed\\\\\\\":true,\\\\\\\"identifier\\\\\\\":\\\\\\\"fakkrina\\\\\\\\u0040gmail.com\\\\\\\",\\\\\\\"user_storage_key\\\\\\\":\\\\\\\"d34f32d5c74eba021c035e5e0e3bb070694500b4f61d15ea29600ad23641b797\\\\\\\",\\\\\\\"is_account_confirmed\\\\\\\":true,\\\\\\\"is_msplit_account\\\\\\\":false,\\\\\\\"is_fb_only_not_allowed_in_msgr\\\\\\\":false,\\\\\\\"is_marketplace_consented\\\\\\\":true,\\\\\\\"is_gaming_consented\\\\\\\":true,\\\\\\\"is_lisa_sso_login\\\\\\\":false,\\\\\\\"credential_type\\\\\\\":\\\\\\\"password\\\\\\\"}\\\", 36, \\\"Password\\\", 38, \\\"Login\\\"), null, (bk.action.core.GetArg, 0)), 1), (bk.action.logging.LogEvent, \\\"caa_login_client_events_fb_msgr\\\", \\\"\\\", (bk.action.map.Make, (bk.action.array.Make, \\\"core\\\", \\\"login_params\\\"), (bk.action.array.Make, (bk.action.map.Make, (bk.action.array.Make, \\\"event\\\", \\\"event_category\\\", \\\"event_flow\\\", \\\"event_request_id\\\", \\\"event_step\\\", \\\"is_dark_mode\\\", \\\"exception_code\\\", \\\"exception_message\\\", \\\"exception_type\\\", \\\"extra_client_data\\\", \\\"extra_server_data_encrypted\\\", \\\"extra_client_data_bks_input\\\", \\\"logged_out_identifier\\\", \\\"logged_in_identifier\\\", \\\"waterfall_id\\\", \\\"reduction_push_phase\\\", \\\"reduction_region\\\", \\\"access_flow_version\\\"), (bk.action.array.Make, \\\"login_success\\\", \\\"login_success\\\", \\\"login_manual\\\", \\\"41543bb8-fd88-4b7b-b316-0a1df5d57ea0\\\", \\\"home_page\\\", (fb.action.IsDarkModeEnabled), 0, \\\"\\\", \\\"\\\", (bk.action.map.Make, (bk.action.array.Make, \\\"login_source\\\", \\\"login_credential_type\\\", \\\"contact_point_type\\\", \\\"is_from_switcher\\\", \\\"fblite_client_id\\\", \\\"is_from_logged_out\\\"), (bk.action.array.Make, \\\"Login\\\", \\\"Password\\\", \\\"email\\\", \\\"0\\\", \\\"\\\", \\\"0\\\")), \\\"ARst6W3EOyb0gVYqKZhzx0HCecewnoLa4OCNoS-OsufWBFMV1Qk0AYRY3ILjFu5KMEMyNORm-HK-U7K3R-lF1tdGebuNFuSl9sQbp9DmVpZWu38nn4TS_4qXy5X6Tf6wDRx9y4m9-rZRD-Jl2JE1UTtDsFlEdQf0ycDbhO6DOiMAzHrPpAH62Z-wLQOnAAxJrEkrS7TPLpwTdSm4BL4HXbBJ2-50bDuvK_OuHku_qZGNNu3K_bHZmpxZ3a0TgJhLjiMS6YvNDcg\\\", (bk.action.map.Make, (bk.action.array.Make), (bk.action.array.Make)), \\\"\\\", \\\"100023854695779\\\", \\\"6b4d97ec-d3e8-4e7a-afe6-8ac6d644f142\\\", \\\"C3\\\", \\\"altoona\\\", \\\"\\\")), (bk.action.map.Make, (bk.action.array.Make), (bk.action.array.Make))))), (bk.action.map.Make, (bk.action.array.Make, \\\"should_dismiss_loading\\\", \\\"has_identification_error\\\"), (bk.action.array.Make, false, false))))\"}}}"}}},"gql_variables":[]}},"extensions":{"server_metadata":{"request_start_time_ms":1716407635420,"time_at_flush_ms":1716407636739},"is_final":true}}
"""