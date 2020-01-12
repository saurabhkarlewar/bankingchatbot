from typing import Any, Text, Dict, List, Union, Optional

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction
# from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
# from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase

# class ActionMyKB(ActionQueryKnowledgeBase):
#     def __init__(self):
#         # load knowledge base with data from the given file
#         knowledge_base = InMemoryKnowledgeBase("knowledge_base_data.json")
#         knowledge_base.set_representation_function_of_object(
#             "transactions", lambda obj: obj["Month"] + " |" + obj["TRANSACTION DETAILS"] + " |" + obj["WITHDRAWAL AMT"] + " |" + obj["DEPOSIT AMT"] + " |" + obj["BALANCE AMT"]
#         )

#         super().__init__(knowledge_base)

class ActionBalanceCheck(Action):

    def name(self) -> Text:
        return "action_balance_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        source_account = tracker.get_slot("source_account")
        phoneno = tracker.get_slot("phoneno")
        dob = tracker.get_slot("dob")
        balance = "$5000"
        dispatcher.utter_message(text="The balance in your account is {}".format(balance))

        return [SlotSet("account_balance",balance)]

class NewProductApplicationForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "new_product_application_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["product", "applicant_name", "applicant_dob", "applicant_phoneno", "applicant_address"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "product": [
                self.from_entity(entity="product", intent=["inform"]),
            ],
            "applicant_name": [
                self.from_entity(entity="applicant_name", intent=["inform"]),
            ],
            "applicant_dob": [
                self.from_entity(entity="applicant_dob", intent=["inform"]),
            ],
            "applicant_phoneno": [
                self.from_entity(entity="applicant_phoneno", intent=["inform"]),
            ],
            "applicant_address": [
                self.from_entity(entity="applicant_address", intent=["inform"]),
            ]
        }

    @staticmethod
    def product_db() -> List[Text]:
        """Database of supported cuisines"""

        return [
            "credit",
            "forex",
            "debit",
            "atm"
        ]

    # USED FOR DOCS: do not rename without updating in docs
    def validate_product(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate cuisine value."""

        if value.lower() in self.product_db():
            # validation succeeded, set the value of the "cuisine" slot to value
            return {"product": value}
        else:
            dispatcher.utter_message(template="utter_wrong_product")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"product": None}

    def validate_application_phoneno(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""

        if self.is_int(value) and int(value) > 0 and int(value) < 100000000000:
            return {"applicant_phoneno": value}
        else:
            dispatcher.utter_message(template="utter_wrong_phone_no")
            # validation failed, set slot to None
            return {"applicant_phoneno": None}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_message(template="utter_submit")
        return []