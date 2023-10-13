from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Boolean,
    Column,
    Integer,
    String,
    Enum,
    Text,
    Date,
    TIMESTAMP,
    ForeignKey,
    text,
    DateTime,
)
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True)


class StaffDetail(Base):
    __tablename__ = "staff_details"
    staff_id = Column(Integer, primary_key=True)
    f_name = Column(String(50), nullable=False)
    l_email = Column(String(50), unique=True, nullable=False)
    dept = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    phone = Column(String(50), nullable=False)
    biz_address = Column(String(255), nullable=False)
    sys_role = Column(
        Enum("staff", "hr", "manager", "inactive"), default="inactive", nullable=False
    )


class SkillDetail(Base):
    __tablename__ = "skill_details"
    skill_id = Column(Integer, primary_key=True)
    skill_name = Column(String(50), nullable=False)
    skill_status = Column(
        Enum("active", "inactive"), default="inactive", nullable=False
    )


class RoleDetail(Base):
    __tablename__ = "role_details"
    role_id = Column(Integer, primary_key=True)
    role_name = Column(String(50), nullable=False)
    role_description = Column(Text, nullable=False)
    role_status = Column(Enum("active", "inactive"), default="inactive", nullable=False)


class StaffReportingOfficer(Base):
    __tablename__ = "staff_reporting_officer"
    staff_id = Column(Integer, ForeignKey("staff_details.staff_id"), primary_key=True)
    RO_id = Column(Integer, ForeignKey("staff_details.staff_id"), primary_key=True)
    staff = relationship("StaffDetail", foreign_keys=[staff_id])
    RO = relationship("StaffDetail", foreign_keys=[RO_id])


class StaffRole(Base):
    __tablename__ = "staff_roles"
    staff_id = Column(
        Integer, ForeignKey("staff_details.staff_id"), primary_key=True, nullable=False
    )
    role_id = Column(
        Integer, ForeignKey("role_details.role_id"), primary_key=True, nullable=False
    )
    role_type = Column(Enum("primary", "secondary"), nullable=False)
    sr_status = Column(Enum("active", "inactive"), default="inactive", nullable=False)
    staff = relationship("StaffDetail")
    role = relationship("RoleDetail")


class StaffSkill(Base):
    __tablename__ = "staff_skills"
    staff_id = Column(
        Integer, ForeignKey("staff_details.staff_id"), primary_key=True, nullable=False
    )
    skill_id = Column(
        Integer, ForeignKey("skill_details.skill_id"), primary_key=True, nullable=False
    )
    ss_status = Column(Enum("active", "unverified", "in-progress"), nullable=False)
    staff = relationship("StaffDetail")
    skill = relationship("SkillDetail")


class RoleSkill(Base):
    __tablename__ = "role_skills"
    role_id = Column(
        Integer, ForeignKey("role_details.role_id"), primary_key=True, nullable=False
    )
    skill_id = Column(
        Integer, ForeignKey("skill_details.skill_id"), primary_key=True, nullable=False
    )
    role = relationship("RoleDetail")
    skill = relationship("SkillDetail")


class RoleApplication(Base):
    __tablename__ = "role_applications"
    role_app_id = Column(Integer, primary_key=True, autoincrement=True)
    role_listing_id = Column(
        Integer, ForeignKey("role_listings.role_listing_id"), nullable=False
    )
    staff_id = Column(Integer, ForeignKey("staff_details.staff_id"), nullable=False)
    role_app_status = Column(Enum("applied", "withdrawn"), nullable=False)
    role_app_reason = Column(Text, nullable=False)
    role_application_ts_create = Column(
        TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"), nullable=False
    )
    role_listing = relationship("RoleListing")
    applicant = relationship("StaffDetail")


class RoleListing(Base):
    __tablename__ = "role_listings"
    role_listing_id = Column(Integer, primary_key=True)
    role_listing_creator = Column(
        Integer, ForeignKey("staff_details.staff_id"), nullable=False
    )
    role_listing_source = Column(
        Integer, ForeignKey("staff_details.staff_id"), nullable=False
    )
    role_listing_updater = Column(
        Integer, ForeignKey("staff_details.staff_id"), nullable=False
    )
    role_id = Column(Integer, ForeignKey("role_details.role_id"), nullable=False)
    role_listing_desc = Column(Text, nullable=False)
    role_listing_open = Column(Date, nullable=False)
    role_listing_close = Column(Date, nullable=False)
    role_listing_ts_create = Column(
        DateTime, server_default=text("CURRENT_TIMESTAMP"), nullable=False
    )
    role_listing_ts_update = Column(
        DateTime, server_default=text("CURRENT_TIMESTAMP"), nullable=False
    )
    creator = relationship("StaffDetail", foreign_keys=[role_listing_creator])
    updater = relationship("StaffDetail", foreign_keys=[role_listing_updater])
    source = relationship("StaffDetail", foreign_keys=[role_listing_source])
    role = relationship("RoleDetail")