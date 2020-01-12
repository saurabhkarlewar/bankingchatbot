## happy path
* greet
  - utter_greet
  - utter_how_can_i_help

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## bot great
* mood_great
  - utter_happy

## search account balance
* balance_check
  - utter_validate_user
  - utter_ask_phoneno
* inform{"phoneno":"9892816075"}
  - utter_ask_dateofbirth
* inform{"dob":"06091985"}
  - utter_ask_source_account
* inform{"source_account":"savings"}
  <!-- - action_balance_search -->
  - utter_did_that_help

## show transaction details stop but continue path
* transaction_details
  - utter_validate_user
  - utter_ask_phoneno
* inform{"phoneno":"9191919191"}
  - utter_ask_dateofbirth
* inform{"dob":"09069187"}
  - utter_ask_source_account
* inform{"source_account":"savings"}
  - action_query_knowledge_base
  - utter_did_that_help

## apply for new product
* apply_for_new_product
  - utter_product_application_init
  - new_product_application_form
  - form{"name": "new_product_application_form"}
  - form{"name": null}
  - utter_slots_values

## apply for new product stop but continue path
* greet
    - utter_greet
* apply_for_new_product
    - utter_product_application_init
    - new_product_application_form
    - form{"name": "new_product_application_form"}
* stop
    - utter_ask_continue
* affirm
    - new_product_application_form
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries

## apply for new product chitchat stop but continue path
* apply_for_new_product
    - utter_product_application_init
    - new_product_application_form
    - form{"name": "new_product_application_form"}
* chitchat
    - utter_chitchat
    - new_product_application_form
* stop
    - utter_ask_continue
* affirm
    - new_product_application_form
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries

## apply for new product stop but continue and chitchat path
* greet
    - utter_greet
* apply_for_new_product
    - utter_product_application_init
    - new_product_application_form
    - form{"name": "new_product_application_form"}
* stop
    - utter_ask_continue
* affirm
    - new_product_application_form
* chitchat
    - utter_chitchat
    - new_product_application_form
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries

## apply for new product chitchat stop but continue and chitchat path
* greet
    - utter_greet
* apply_for_new_product
    - utter_product_application_init
    - new_product_application_form
    - form{"name": "new_product_application_form"}
* chitchat
    - utter_chitchat
    - new_product_application_form
* stop
    - utter_ask_continue
* affirm
    - new_product_application_form
* chitchat
    - utter_chitchat
    - new_product_application_form
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries

## chitchat, stop and really stop path
* greet
    - utter_greet
* apply_for_new_product
    - utter_product_application_init
    - new_product_application_form
    - form{"name": "new_product_application_form"}
* chitchat
    - utter_chitchat
    - new_product_application_form
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}