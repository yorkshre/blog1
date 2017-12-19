from ..models.user import User


class UserService(object):

    @classmethod
    def by_name(cls, name, request):
        return request.dbsession.query(User).filter(User.name == name).first()

    @classmethod
    def by_id(cls, id_, request):
        return request.dbsession.query(User).filter(User.id == id_).first()
