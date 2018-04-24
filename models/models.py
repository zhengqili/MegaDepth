
def create_model(opt):
    model = None
    from .HG_model import HGModel
    model = HGModel(opt)
    print("model [%s] was created" % (model.name()))
    return model
