KEY_SUMMARY_INSIGHT = "summary_insight"
KEY_NEXT_STEP = "next_step"

DOMAIN_LEVEL_SUMMARY_INSIGHTS = {
    "discipleship": {
        1: "Missions is not yet a visible or structured part of your church’s discipleship life.",
        2: "There is growing awareness of missions, but discipleship and training remain exploratory.",
        3: "Missions is present in teaching and discipleship, with early efforts at integration.",
        4: "Missions is actively taught and supported with structured equipping.",
        5: "Missions is deeply embedded into your church’s discipleship culture and training systems.",
    },
    "sending": {
        1: "Sending has not yet begun and there are no systems or awareness in place.",
        2: "Interest is growing, and some individuals are exploring missions.",
        3: "Short- and mid-term sending is happening ad-hoc or informally.",
        4: "Sending systems are established and supported by leadership.",
        5: "Sending is strategic, proactive, and part of your church's long-term vision.",
    },
    "support": {
        1: "Missions support (prayer, giving, community) is minimal and not prioritised.",
        2: "Giving and praying are starting to be encouraged, but inconsistently.",
        3: "A culture of generosity and prayer is growing. Community life is forming.",
        4: "Support systems are strong and mission-focused.",
        5: "Your church embodies a culture of missional generosity and prayerful support.",
    },
    "structure": {
        1: "There is no missions leadership structure, policies, or partnerships.",
        2: "Leaders are beginning to engage missions ideas and explore structures.",
        3: "Some leadership structures or committees are forming.",
        4: "Missions governance, policies, and partnerships are stabilising.",
        5: "A strong, resourced missions structure supports long-term effectiveness.",
    },
}

SUBDOMAIN_LEVEL_TEXT_CONTENT = {
    "education": {
        1: {
            KEY_SUMMARY_INSIGHT: "Missions is rarely visible in your worship or discipleship settings.",
            KEY_NEXT_STEP: "Introduce quarterly missions-focused elements in worship (e.g. prayer, stories, short messages). Use these to gently shape awareness and engagement.",
        },
        2: {
            KEY_SUMMARY_INSIGHT: "Missions appears occasionally and is beginning to gain traction.",
            KEY_NEXT_STEP: "Schedule bi-monthly prayer for nations or mission updates. Encourage your teaching team to reference missions themes from Scripture.",
        },
        3: {
            KEY_SUMMARY_INSIGHT: "Missions is gaining a foothold in pulpit and discipleship settings.",
            KEY_NEXT_STEP: "Build a rhythm: e.g., preach a missions series yearly and integrate prayer for nations in cell groups.",
        },
        4: {
            KEY_SUMMARY_INSIGHT: "Missions is featured regularly across discipleship platforms.",
            KEY_NEXT_STEP: "Develop curated resources for cell leaders and teachers to reinforce missions themes consistently.",
        },
        5: {
            KEY_SUMMARY_INSIGHT: "Missions is central to spiritual formation across your church.",
            KEY_NEXT_STEP: "Engage with leaders in other churches by sharing how you’ve integrated missions into your worship life and disciple-making process.",
        },
    },
    "training": {
        1: {
            KEY_SUMMARY_INSIGHT: "No structured missions training is available currently.",
            KEY_NEXT_STEP: "Recommend external courses (e.g. Kairos, Perspectives) to interested members. Identify 1 to 2 potential trainers in your church.",
        },
        2: {
            KEY_SUMMARY_INSIGHT: "Leaders refer members to training opportunities externally.",
            KEY_NEXT_STEP: "Invite a missions trainer to conduct an intro workshop in-house. Capture feedback and gauge readiness to scale up.",
        },
        3: {
            KEY_SUMMARY_INSIGHT: "Training efforts are emerging, with in-house ideas forming.",
            KEY_NEXT_STEP: "Pilot a short-term training module (e.g., 3–4 weeks) and align with your next mission trip or event.",
        },
        4: {
            KEY_SUMMARY_INSIGHT: "You have a structured training system, and candidates are being equipped.",
            KEY_NEXT_STEP: "Ensure your pipeline includes mentorship and exposure trips. Consider adding modules on tentmaking or Business-as-missions.",
        },
        5: {
            KEY_SUMMARY_INSIGHT: "You actively train and disciple members toward long-term missions.",
            KEY_NEXT_STEP: "Share your training resources with others. Explore collaborations with seminaries or regional partners.",
        },
    },
    "sending1": {
        1: {
            KEY_SUMMARY_INSIGHT: "Your church has not begun sending members cross-culturally.",
            KEY_NEXT_STEP: "Build awareness by inviting missionary speakers and running vision nights. Consider joining another church’s team for a first exposure trip.",
        },
        2: {
            KEY_SUMMARY_INSIGHT: "Some members are exploring missions independently.",
            KEY_NEXT_STEP: "Create a basic pathway document outlining options for ST/MT/LT sending and how your church can support.",
        },
        3: {
            KEY_SUMMARY_INSIGHT: "You are sending teams or individuals on an ad-hoc basis.",
            KEY_NEXT_STEP: "Start tracking sending activity. Partner with agencies for training and supervision.",
        },
        4: {
            KEY_SUMMARY_INSIGHT: "A regular sending rhythm and policy are in place.",
            KEY_NEXT_STEP: "Set clear sending goals (e.g., 1 ST team per year). Equip pastoral staff to oversee preparation and re-entry.",
        },
        5: {
            KEY_SUMMARY_INSIGHT: "Your church has an active strategy to identify and send missionaries.",
            KEY_NEXT_STEP: "Multiply efforts into new demographics (e.g. youth, retirees). Explore collaborative cross-church sending models.",
        },
    },
    "membercare": {
        1: {
            KEY_SUMMARY_INSIGHT: "There is currently no structure for missionary care.",
            KEY_NEXT_STEP: "Begin pastoral check-ins with missionaries (past or present). Signal care through small acts like sending updates and prayer.",
        },
        2: {
            KEY_SUMMARY_INSIGHT: "Some informal care is present but lacks structure.",
            KEY_NEXT_STEP: "Form a care team and assign each missionary a point person. Provide updates to the wider church.",
        },
        3: {
            KEY_SUMMARY_INSIGHT: "Church leaders are beginning to provide intentional care.",
            KEY_NEXT_STEP: "Develop basic policies for care before, during, and after field deployment. Include families in the care plan.",
        },
        4: {
            KEY_SUMMARY_INSIGHT: "Care teams are active, and systems are developing.",
            KEY_NEXT_STEP: "Train care teams in topics like burnout, re-entry and trauma. Explore partnerships with member care agencies.",
        },
        5: {
            KEY_SUMMARY_INSIGHT: "Member care is holistic and integrated across your church.",
            KEY_NEXT_STEP: "Document your model and support other churches seeking to develop similar care frameworks.",
        },
    },
    "praying": {
        1: {
            KEY_SUMMARY_INSIGHT: "Missions prayer is almost absent from services or meetings.",
            KEY_NEXT_STEP: "Introduce a monthly “prayer for the nations” segment during service. Use global prayer tools (e.g. Operation World).",
        },
        2: {
            KEY_SUMMARY_INSIGHT: "Some prayer for missions is present but infrequent.",
            KEY_NEXT_STEP: "Schedule a quarterly prayer night for missions. Share prayer points from missionaries and agencies.",
        },
        3: {
            KEY_SUMMARY_INSIGHT: "Missions prayer occurs regularly e.g. monthly in meetings.",
            KEY_NEXT_STEP: "Encourage cell groups to “adopt” a nation or missionary to pray for regularly.",
        },
        4: {
            KEY_SUMMARY_INSIGHT: "Missions prayer is strategic and frequent.",
            KEY_NEXT_STEP: "Develop seasonal prayer themes (e.g., Ramadan, persecuted church) and empower prayer leaders to lead intercession.",
        },
        5: {
            KEY_SUMMARY_INSIGHT: "Prayer for missions is deeply integrated into your church life.",
            KEY_NEXT_STEP: "Start a missions prayer network or WhatsApp broadcast to mobilise wider participation. Train new leaders.",
        },
    },
    "giving": {
        1: {
            KEY_SUMMARY_INSIGHT: "Missions giving is not prioritised in your budget or teaching.",
            KEY_NEXT_STEP: "Start by setting aside a small fixed % (e.g. 5–10%) for missions. Communicate why this matters biblically.",
        },
        2: {
            KEY_SUMMARY_INSIGHT: "Missions giving happens occasionally for special appeals.",
            KEY_NEXT_STEP: "Launch a missions faith pledge campaign or giving drive to increase regular support.",
        },
        3: {
            KEY_SUMMARY_INSIGHT: "Teaching on generosity for missions is beginning to take root.",
            KEY_NEXT_STEP: "Teach on sacrificial generosity during missions emphasis months. Provide giving updates to the church.",
        },
        4: {
            KEY_SUMMARY_INSIGHT: "Missions giving is consistent and encouraged.",
            KEY_NEXT_STEP: "Review giving policies to ensure sustainability and avoid dependency.",
        },
        5: {
            KEY_SUMMARY_INSIGHT: "Your church has a healthy and generous missions giving culture.",
            KEY_NEXT_STEP: "Share your giving model with other churches and encourage collaboration in funding large-scale efforts.",
        },
    },
    "community": {
        1: {
            KEY_SUMMARY_INSIGHT: "There is no identifiable missions community in your church.",
            KEY_NEXT_STEP: "Identify members with a heart for missions and start gathering quarterly to pray and share.",
        },
        2: {
            KEY_SUMMARY_INSIGHT: "A small group is forming, usually informal.",
            KEY_NEXT_STEP: "Empower a leader to convene gatherings and liaise with the church leadership.",
        },
        3: {
            KEY_SUMMARY_INSIGHT: "The missions community is growing and meeting regularly.",
            KEY_NEXT_STEP: "Involve the missions community in planning events, prayer nights, or ST trips.",
        },
        4: {
            KEY_SUMMARY_INSIGHT: "A strong and engaged missions community is in place.",
            KEY_NEXT_STEP: "Launch a mentoring program pairing senior missions advocates with new members.",
        },
        5: {
            KEY_SUMMARY_INSIGHT: "The missions community is active, reproducing, and outward-facing.",
            KEY_NEXT_STEP: "Multiply this group’s impact by catalysing missions engagement across ministries and demographics.",
        },
    },
    "organisation": {
        1: {
            KEY_SUMMARY_INSIGHT: "Missions is not yet prioritised by leadership or staffing.",
            KEY_NEXT_STEP: "Share your CMRA results with senior leadership and begin regular conversations about church vision for missions.",
        },
        2: {
            KEY_SUMMARY_INSIGHT: "A few leaders are beginning to engage in missions.",
            KEY_NEXT_STEP: "Identify a point person for missions within staff or board. Begin forming a working committee.",
        },
        3: {
            KEY_SUMMARY_INSIGHT: "You have early structures like a staff contact or committee.",
            KEY_NEXT_STEP: "Clarify the role of your committee and draft a basic charter or ministry mandate.",
        },
        4: {
            KEY_SUMMARY_INSIGHT: "Leadership teams and staff are engaged and active.",
            KEY_NEXT_STEP: "Consider succession planning and developing a training pathway for new leaders.",
        },
        5: {
            KEY_SUMMARY_INSIGHT: "Missions is fully owned at the leadership level.",
            KEY_NEXT_STEP: "Share your model with other churches. Multiply missions leadership into youth and other departments.",
        },
    },
    "policies": {
        1: {
            KEY_SUMMARY_INSIGHT: "No missions-related policies are in place.",
            KEY_NEXT_STEP: "Begin drafting a missions philosophy statement and a short-term trips policy template.",
        },
        2: {
            KEY_SUMMARY_INSIGHT: "Basic conversations are underway around policies.",
            KEY_NEXT_STEP: "Research other churches’ policies for LT sending and adapt to your context.",
        },
        3: {
            KEY_SUMMARY_INSIGHT: "Working policies are present but may be outdated.",
            KEY_NEXT_STEP: "Review and revise existing policies. Involve sent missionaries in feedback.",
        },
        4: {
            KEY_SUMMARY_INSIGHT: "Policies are robust and regularly updated.",
            KEY_NEXT_STEP: "Add specialised frameworks for tentmaking, Business-as-missions, or bi-vocational sending.",
        },
        5: {
            KEY_SUMMARY_INSIGHT: "You have comprehensive and forward-looking missions policies.",
            KEY_NEXT_STEP: "Document and share your policies through denominational or network platforms.",
        },
    },
    "partnerships": {
        1: {
            KEY_SUMMARY_INSIGHT: "Your church currently has no missions partnerships.",
            KEY_NEXT_STEP: "Identify one reputable agency or church to begin conversations with.",
        },
        2: {
            KEY_SUMMARY_INSIGHT: "You’re starting to build relationships with agencies.",
            KEY_NEXT_STEP: "Formalise your first partnership — e.g. agree on a sending or training collaboration.",
        },
        3: {
            KEY_SUMMARY_INSIGHT: "You have working relationships that support church missions.",
            KEY_NEXT_STEP: "Evaluate partnership outcomes annually and ensure mutual value.",
        },
        4: {
            KEY_SUMMARY_INSIGHT: "Partnerships are healthy, productive, and missionally aligned.",
            KEY_NEXT_STEP: "Consider expanding your footprint by investing in new regions or church networks.",
        },
        5: {
            KEY_SUMMARY_INSIGHT: "Your partnerships are strategic and catalytic.",
            KEY_NEXT_STEP: "Collaborate with other churches for regional missions strategies and joint sending efforts.",
        },
    },
}
