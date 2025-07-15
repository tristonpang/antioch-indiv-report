from enum import Enum

FieldIds = Enum(
    "FieldIds",
    [
        ("respondent", "Wz6EJ0SrP537"),
        ("email", "mQQ6n4XODVE8"),
        ("role", "7rGpb91gC5Zv"),
        ("church", "4yBh92Cyp8hz"),
    ],
)


class FormResponseAnswersFields:
    def __init__(self, **kwargs):
        self.respondent = kwargs.get("respondent")
        self.email = kwargs.get("email")
        self.role = kwargs.get("role")
        self.church = kwargs.get("church")


class FormResponseScores:
    def __init__(self, **kwargs):
        self.community = kwargs.get("community")
        self.discipleship = kwargs.get("discipleship")
        self.education = kwargs.get("education")
        self.finalpercentage = kwargs.get("finalpercentage")
        self.giving = kwargs.get("giving")
        self.membercare = kwargs.get("membercare")
        self.organisation = kwargs.get("organisation")
        self.partnerships = kwargs.get("partnerships")
        self.policies = kwargs.get("policies")
        self.praying = kwargs.get("praying")
        self.score = kwargs.get("score")
        self.sending = kwargs.get("sending")
        self.sending1 = kwargs.get("sending1")
        self.structure = kwargs.get("structure")
        self.support = kwargs.get("support")
        self.training = kwargs.get("training")


class FormResponse:
    def map_scores_args(self, raw_scores):
        args_for_scores = dict()
        for score in raw_scores:
            args_for_scores[score["key"]] = score["number"]
        return args_for_scores

    def __init__(self, raw_response):
        # self.response_id = raw_response["response_id"]
        # self.response_type = raw_response["response_type"]

        # Form response answers
        args_for_answers = dict()
        for answer in raw_response["answers"]:
            try:
                field_name = FieldIds(answer["field"]["id"]).name
                args_for_answers[field_name] = (
                    answer["text"] if answer["type"] == "text" else answer["email"]
                )
            except:
                continue
        self.answers = FormResponseAnswersFields(**args_for_answers)

        # Form response scores
        args_for_scores = self.map_scores_args(raw_response["scores"])
        self.scores = FormResponseScores(**args_for_scores)
