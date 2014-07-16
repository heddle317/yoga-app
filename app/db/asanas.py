import datetime

from app.db import app_db as db
from app.db import delete
from app.db import get
from app.db import get_list
from app.db import save
from app.db import update
from app.utils.datetime_tools import format_date
from app.utils.datetime_tools import relative_time

from sqlalchemy.dialects.postgresql import UUID

from uuid import uuid4


REQUIRED_FIELDS = ['name']


class Asana(db.Model):
    __tablename__ = 'asanas'
    uuid = db.Column(UUID, primary_key=True)
    name = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime(), unique=False, default=datetime.datetime.utcnow())

    def to_dict(self):
        # get images
        images = AsanaImage.get_asana_images(self.uuid)
        # get attributes
        attributes = AsanaAttribute.get_asana_attributes(self.uuid)
        print self.created_at
        data = {'uuid': self.uuid,
                'name': self.name,
                'created_ago': relative_time(self.created_at),
                'created_at': format_date(self.created_at, format='%B %d, %Y'),
                'image_url': get(AsanaImage, asana_uuid=self.uuid, primary_image=True).image_url,
                'images': images,
                'description': get(AsanaAttribute, asana_uuid=self.uuid, name='description').value,
                'attributes': attributes
                }
        return data

    @staticmethod
    def get_asanas():
        return [asana.to_dict() for asana in get_list(Asana)]

    @staticmethod
    def get_asana(uuid):
        return get(Asana, uuid=uuid).to_dict()

    @staticmethod
    def create_asana(**kwargs):
        for field in REQUIRED_FIELDS:
            if not kwargs.get(field):
                raise ValueError('%s required' % field)
        asana = Asana(uuid=str(uuid4()),
                      name=kwargs.pop('name', ''))
        asana = save(asana)
        # create image
        AsanaImage.create_asana_image(asana.uuid, kwargs.get('image_url'), True)
        # create attributes
        for name in kwargs.keys():
            AsanaAttribute.create_asana_attribute(asana.uuid, name, kwargs.get(name))
        return asana.to_dict()

    @staticmethod
    def update_asana(uuid, **kwargs):
        asana = get(Asana, uuid)
        update(asana, **kwargs)
        return asana.to_dict()

    @staticmethod
    def delete_asana(uuid):
        asana = get(Asana, uuid=uuid)
        delete(asana)


class AsanaAttribute(db.Model):
    __tablename__ = 'asana_attributes'
    uuid = db.Column(UUID, primary_key=True, nullable=False)
    asana_uuid = db.Column(UUID, nullable=False)
    name = db.Column(db.String(500), nullable=False)
    value = db.Column(db.String(500), nullable=True)
    created_at = db.Column(db.DateTime(), unique=False, default=datetime.datetime.utcnow())

    def to_dict(self):
        return {'uuid': self.uuid,
                'asana_uuid': self.asana_uuid,
                'name': self.name,
                'value': self.value,
                'created_at': format_date(self.created_at, format='%B %d, %Y')
                }

    @staticmethod
    def get_asana_attributes(asana_uuid):
        return [asana_attribute.to_dict() for asana_attribute in get_list(AsanaAttribute, asana_uuid=asana_uuid)]

    @staticmethod
    def get_asana_attribute(uuid):
        return get(AsanaAttribute, uuid=uuid).to_dict()

    @staticmethod
    def create_asana_attribute(asana_uuid, name, value):
        asana_attribute = AsanaAttribute(uuid=str(uuid4()),
                                         asana_uuid=asana_uuid,
                                         name=name,
                                         value=value)
        asana_attribute = save(asana_attribute)
        return asana_attribute.to_dict()

    @staticmethod
    def update_asana_attribute(uuid, **kwargs):
        asana_attribute = get(AsanaAttribute, uuid)
        update(asana_attribute, **kwargs)
        return asana_attribute.to_dict()

    @staticmethod
    def delete_asana_attribute(uuid):
        asana_attribute = get(AsanaAttribute, uuid=uuid)
        delete(asana_attribute)


class AsanaImage(db.Model):
    __tablename__ = 'asana_images'
    uuid = db.Column(UUID, primary_key=True, nullable=False)
    asana_uuid = db.Column(UUID, nullable=False)
    image_url = db.Column(db.String(500), nullable=False)
    primary_image = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime(), unique=False, default=datetime.datetime.utcnow())

    def to_dict(self):
        return {'uuid': self.uuid,
                'asana_uuid': self.asana_uuid,
                'image_url': self.image_url,
                'primary_image': self.primary_image,
                'created_at': format_date(self.created_at, format='%B %d, %Y')
                }

    @staticmethod
    def get_asana_images(asana_uuid):
        return [asana_image.to_dict() for asana_image in get_list(AsanaImage, asana_uuid=asana_uuid)]

    @staticmethod
    def get_asana_image(uuid):
        return get(AsanaImage, uuid=uuid).to_dict()

    @staticmethod
    def create_asana_image(asana_uuid, image_url, primary_image=False):
        asana_image = AsanaImage(uuid=str(uuid4()),
                                 asana_uuid=asana_uuid,
                                 image_url=image_url,
                                 primary_image=primary_image)
        asana_image = save(asana_image)
        return asana_image.to_dict()

    @staticmethod
    def update_asana_image(uuid, **kwargs):
        asana_image = get(AsanaImage, uuid)
        update(asana_image, **kwargs)
        return asana_image.to_dict()

    @staticmethod
    def delete_asana_image(uuid):
        asana_image = get(AsanaImage, uuid=uuid)
        delete(asana_image)
