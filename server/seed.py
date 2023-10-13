from models import (
    StaffDetail,
    SkillDetail,
    RoleDetail,
    StaffReportingOfficer,
    StaffRole,
    StaffSkill,
    RoleSkill,
    RoleApplication,
    RoleListing,
)


staff_details_seed = [
    {
        "staff_id": 123456789,
        "f_name": "AH GAO",
        "l_email": "TAN",
        "dept": "FINANCE",
        "email": "tan_ah_gao@all-in-one.com.sg",
        "phone": "65-1234-5678",
        "biz_address": "60 Paya Lebar Rd, #06-33 Paya Lebar Square, Singapore 409051",
        "sys_role": "staff",
    },
    {
        "staff_id": 123456788,
        "f_name": "VINCENT REX",
        "l_email": "COLINS",
        "dept": "HUMAN RESOURCE AND ADMIN",
        "email": "colins_vincent_rex@all-in-one.com.sg",
        "phone": "65-1234-5679",
        "biz_address": "60 Paya Lebar Rd, #06-33 Paya Lebar Square, Singapore 409051",
        "sys_role": "hr",
    },
    {
        "staff_id": 123456787,
        "f_name": "FAUD",
        "l_email": "NIZAM",
        "dept": "SALES",
        "email": "faud_nizam@all-in-one.com.sg",
        "phone": "60-03-21345678",
        "biz_address": "Unit 3A-07, Tower A, The Vertical Business Suite, 8, Jalan Kerinchi, Bangsar South, 59200 Kuala Lumpur, Malaysia",
        "sys_role": "manager",
    },
    {
        "staff_id": 123456786,
        "f_name": "JOHN",
        "l_email": "DOE",
        "dept": "IT",
        "email": "John_doe@all-in-one.com.sg",
        "phone": "65-5824-7888",
        "biz_address": "1 Scotts Rd, #24-10 Shaw Centre, Singapore 228208",
        "sys_role": "inactive",
    },
    {
        "staff_id": 1,
        "f_name": "ROOT",
        "l_email": "ADMIN",
        "dept": "IT",
        "email": "rootme@all-in-one.com.sg",
        "phone": "65-5824-7888",
        "biz_address": "1 Scotts Rd, #24-10 Shaw Centre, Singapore 228208",
        "sys_role": "staff",
    },
    {
        "staff_id": 123456123,
        "f_name": "ROOT",
        "l_email": "ADMIN SECOND",
        "dept": "IT",
        "email": "rootme2@all-in-one.com.sg",
        "phone": "65-5824-7888",
        "biz_address": "1 Scotts Rd, #24-10 Shaw Centre, Singapore 228208",
        "sys_role": "staff",
    },
]
skill_details_seed = [
    {
        "skill_id": 345678912,
        "skill_name": "Pascal Programming",
        "skill_status": "inactive",
    },
    {
        "skill_id": 345678913,
        "skill_name": "Python Programming",
        "skill_status": "active",
    },
    {
        "skill_id": 345678914,
        "skill_name": "Certified Scrum Master",
        "skill_status": "active",
    },
    {
        "skill_id": 345678915,
        "skill_name": "Certified Scrum Product Owner",
        "skill_status": "active",
    },
    {
        "skill_id": 345678866,
        "skill_name": "Certified Scrum Developer",
        "skill_status": "active",
    },
    {
        "skill_id": 345678790,
        "skill_name": "Certified Scrum Professional",
        "skill_status": "active",
    },
    {
        "skill_id": 345678935,
        "skill_name": "Certified Scrum Trainer",
        "skill_status": "active",
    },
    {
        "skill_id": 345678927,
        "skill_name": "Certified Scrum Coach",
        "skill_status": "active",
    },
    {
        "skill_id": 345678890,
        "skill_name": "Certified Scrum@Scale Practitioner",
        "skill_status": "active",
    },
]
role_details_seed = [
    {
        "role_id": 234567891,
        "role_name": "Head, Talent Attraction",
        "role_description": "The Head, Talent Attraction is responsible for strategic workforce planning to support the organisation's growth strategies through establishing talent sourcing strategies, determining the philosophy for the selection and securing of candidates and overseeing the onboarding and integration of new hires into the organisation. He/She develops various approaches to meet workforce requirements and designs employer branding strategies. He oversees the selection processes and collaborates with business stakeholders for the hiring of key leadership roles. As a department head, he is responsible for setting the direction and articulating goals and objectives for the team, and driving the integration of Skills Frameworks across the organisation's talent attraction plans. The Head, Talent Attraction is an influential and inspiring leader who adopts a broad perspective in the decisions he makes. He is articulate and displays a genuine passion for motivating and developing his team.",
        "role_status": "inactive",
    },
    {
        "role_id": 234567892,
        "role_name": "Learning Facilitator / Trainer",
        "role_description": "The Learning Facilitator delivers learning products and services in a variety of environments, using multiple learning delivery modes and methods. He/She assesses learning needs and adapts the facilitation approach to reflect desired learning outcomes and learner needs. He is responsible for knowledge and skills transfer by delivering learning content, facilitating group discussions and responding to queries. He drives learner development and commitment to continuous learning by actively providing feedback and learner support. He evaluates curriculum effectiveness and recommends improvement areas by collecting learner feedback as well as analysing learning delivery approaches and materials.He is a strong communicator who builds trusted relationships and creates a cooperative and engaging learning environment. He is adaptable and adept at managing multiple stakeholders. He works in multiple different environments, including different learning venues and client sites, and regularly interacts with digital systems.",
        "role_status": "active",
    },
    {
        "role_id": 234567893,
        "role_name": "Agile Coach (SM)",
        "role_description": "The Agile Coach (SM) coaches teams in the conduct of Agile practices and the implementation of Agile methodologies and practices in the organisation and acts as an effective Scrum Master in Agile Scrum teams.",
        "role_status": "active",
    },
    {
        "role_id": 234511581,
        "role_name": "Fire Warden",
        "role_description": "The Fire Warden is responsible for testing fire alarms and firefighting equipment and implementing risk assessment recommendations. In the event of a confirmed fire alarm or fire drill, the warden assists in the safe evacuation of staff and visitors from the premise immediately.",
        "role_status": "active",
    },
]
staff_reporting_officer_seed = [
    {"staff_id": 123456789, "RO_id": 123456123},
    {"staff_id": 123456123, "RO_id": 1},
]
staff_roles_seed = [
    {
        "staff_id": 123456789,
        "role_id": 234567891,
        "role_type": "primary",
        "sr_status": "active",
    },
    {
        "staff_id": 123456789,
        "role_id": 234567893,
        "role_type": "secondary",
        "sr_status": "active",
    },
    {
        "staff_id": 123456789,
        "role_id": 234511581,
        "role_type": "secondary",
        "sr_status": "active",
    },
]
staff_skills_seed = [
    {"staff_id": 123456789, "skill_id": 345678913, "ss_status": "active"},
    {"staff_id": 123456789, "skill_id": 345678866, "ss_status": "active"},
    {"staff_id": 123456789, "skill_id": 345678790, "ss_status": "active"},
    {"staff_id": 123456789, "skill_id": 345678890, "ss_status": "unverified"},
    {"staff_id": 123456789, "skill_id": 345678935, "ss_status": "in-progress"},
    {"staff_id": 123456789, "skill_id": 345678927, "ss_status": "in-progress"},
]
role_skills_seed = [
    {"role_id": 234567893, "skill_id": 345678935},
    {"role_id": 234567892, "skill_id": 345678913},
    {"role_id": 234567892, "skill_id": 345678912},
]
role_applications_seed = [
    {
        "role_listing_id": 1,
        "staff_id": 123456789,
        "role_app_status": "applied",
        "role_app_reason": "I want to apply for this role because I am interested in it.",
    },
    {
        "role_listing_id": 2,
        "staff_id": 123456789,
        "role_app_status": "applied",
        "role_app_reason": "I want to apply for this role because I don't know what it is.",
    },
    {
        "role_listing_id": 3,
        "staff_id": 123456789,
        "role_app_status": "applied",
        "role_app_reason": "I want to apply for this role because I want to learn more about it.",
    },
]
role_listings_seed = [
    {
        "role_listing_id": 1,
        "role_listing_creator": 123456789,
        "role_listing_source": 123456789,
        "role_listing_updater": 123456789,
        "role_id": 234567893,
        "role_listing_desc": "The Agile Coach (SM) coaches teams in the conduct of Agile practices and the implementation of Agile methodologies and practices in the organisation and acts as an effective Scrum Master in Agile Scrum teams.",
        "role_listing_open": "2020-01-01",
        "role_listing_close": "2020-01-31",
    },
    {
        "role_listing_id": 2,
        "role_listing_creator": 123456789,
        "role_listing_source": 123456789,
        "role_listing_updater": 123456789,
        "role_id": 234567892,
        "role_listing_desc": "The Learning Facilitator delivers learning products and services in a variety of environments, using multiple learning delivery modes and methods. He/She assesses learning needs and adapts the facilitation approach to reflect desired learning outcomes and learner needs. He is responsible for knowledge and skills transfer by delivering learning content, facilitating group discussions and responding to queries. He drives learner development and commitment to continuous learning by actively providing feedback and learner support. He evaluates curriculum effectiveness and recommends improvement areas by collecting learner feedback as well as analysing learning delivery approaches and materials.He is a strong communicator who builds trusted relationships and creates a cooperative and engaging learning environment. He is adaptable and adept at managing multiple stakeholders. He works in multiple different environments, including different learning venues and client sites, and regularly interacts with digital systems.",
        "role_listing_open": "2020-01-01",
        "role_listing_close": "2020-01-31",
    },
    {
        "role_listing_id": 3,
        "role_listing_creator": 123456789,
        "role_listing_source": 123456789,
        "role_listing_updater": 123456789,
        "role_id": 234567891,
        "role_listing_desc": "The Head, Talent Attraction is responsible for strategic workforce planning to support the organisation's growth strategies through establishing talent sourcing strategies, determining the philosophy for the selection and securing of candidates and overseeing the onboarding and integration of new hires into the organisation. He/She develops various approaches to meet workforce requirements and designs employer branding strategies. He oversees the selection processes and collaborates with business stakeholders for the hiring of key leadership roles. As a department head, he is responsible for setting the direction and articulating goals and objectives for the team, and driving the integration of Skills Frameworks across the organisation's talent attraction plans. The Head, Talent Attraction is an influential and inspiring leader who adopts a broad perspective in the decisions he makes. He is articulate and displays a genuine passion for motivating and developing his team.",
        "role_listing_open": "2020-01-01",
        "role_listing_close": "2020-01-31",
    },
]


def seed_db(session):
    for detail in staff_details_seed:
        staff_details = StaffDetail(**detail)
        session.add(staff_details)

    for detail in skill_details_seed:
        skill_details = SkillDetail(**detail)
        session.add(skill_details)

    for detail in role_details_seed:
        role_details = RoleDetail(**detail)
        session.add(role_details)

    for detail in staff_reporting_officer_seed:
        staff_reporting_officer = StaffReportingOfficer(**detail)
        session.add(staff_reporting_officer)

    for detail in staff_roles_seed:
        staff_roles = StaffRole(**detail)
        session.add(staff_roles)

    for detail in staff_skills_seed:
        staff_skills = StaffSkill(**detail)
        session.add(staff_skills)

    for detail in role_skills_seed:
        role_skills = RoleSkill(**detail)
        session.add(role_skills)

    for detail in role_listings_seed:
        role_listings = RoleListing(**detail)
        session.add(role_listings)

    for detail in role_applications_seed:
        role_applications = RoleApplication(**detail)
        session.add(role_applications)

    session.commit()
    session.close()
