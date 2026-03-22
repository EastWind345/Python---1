import pytest
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    is_active = Column(Boolean, default=True)


@pytest.fixture
def setup_teardown(session):
    Base.metadata.create_all(session.get_bind())
    yield
    Base.metadata.drop_all(session.get_bind())


def test_create_student(session, setup_teardown):
    """Тест на добавление студента"""
    student = Student(name="Alena Rock")
    session.add(student)
    session.commit()

    result = session.query(Student).filter_by(name="Alena Rock").first()
    assert result is not None
    assert result.name == "Alena Rock"


def test_update_student(session, setup_teardown):
    """Тест на изменение студента"""
    student = Student(name="Eva Star")
    session.add(student)
    session.commit()

    student.name = "Eva Gold"
    session.commit()

    updated = session.query(Student).get(student.id)
    assert updated.name == "Eva Gold"


def test_soft_delete_student(session, setup_teardown):
    """Тест на мягкое удаление студента"""
    student = Student(name="Anna Top")
    session.add(student)
    session.commit()

    student.is_active = False
    session.commit()

    deleted = session.query(Student).get(student.id)
    assert deleted.is_active is False
