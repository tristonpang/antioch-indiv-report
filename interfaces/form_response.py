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
        # Domain 1: Discipleship
        self.discipleship = kwargs.get("discipleship")
        self.education = kwargs.get("education")
        self.training = kwargs.get("training")

        # Domain 2: Sending
        self.sending = kwargs.get("sending")
        self.sending1 = kwargs.get("sending1")
        self.membercare = kwargs.get("membercare")

        # Domain 3: Support
        self.support = kwargs.get("support")
        self.praying = kwargs.get("praying")
        self.giving = kwargs.get("giving")
        self.community = kwargs.get("community")

        # Domain 4: Structure
        self.structure = kwargs.get("structure")
        self.organisation = kwargs.get("organisation")
        self.policies = kwargs.get("policies")
        self.partnerships = kwargs.get("partnerships")

        ranked_scores = [
            ("discipleship", self.discipleship),
            ("education", self.education),
            ("training", self.training),
            ("sending", self.sending),
            ("sending1", self.sending1),
            ("membercare", self.membercare),
            ("support", self.support),
            ("praying", self.praying),
            ("giving", self.giving),
            ("community", self.community),
            ("structure", self.structure),
            ("organisation", self.organisation),
            ("policies", self.policies),
            ("partnerships", self.partnerships),
        ]
        ranked_scores.sort(key=lambda x: x[1], reverse=True)

        self.top_3_strongest_subdomains = [ranked_scores[i] for i in range(3)]
        self.bottom_3_weakest_subdomains = [
            ranked_scores[i]
            for i in range(len(ranked_scores) - 1, len(ranked_scores) - 4, -1)
        ]

        self.score = kwargs.get("score")
        self.finalpercentage = kwargs.get("finalpercentage")


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
