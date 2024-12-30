from pydrake.all import (Parser, MultibodyPlant, RigidTransform)

def AddAndWeldModelFromUrl(
        model_url,
        model_name,
        parent,
        child_frame_name,
        X_PC,
        plant):
    parser = Parser(plant, model_name)
    new_model = parser.AddModelsFromUrl(model_url)
    # new_model.name = model_name
    child_frame = plant.GetFrameByName(
            child_frame_name,
            plant.GetModelInstanceName(model_name))
    plant.WeldFrames(parent, child_frame, X_PC)
    return new_model

def CreateIiwaPlant():
    plant = MultibodyPlant(1e-3)
    parser = Parser(plant=plant)
    directives = "./iiwa7.dmd.yaml"
    robot_model_indices = parser.AddModels(directives)

    # iiwa_drake_url = (
    #     "package://drake_models/iiwa_description/sdf/iiwa7_no_collision.sdf")
    # iiwa_path = pydrake.common.FindResourceOrThrow(iiwa_drake_path)
    # robot_model = parser.AddModelFromFile(iiwa_path)
    # robot_model = AddAndWeldModelFromUrl(
    #         iiwa_drake_url, "iiwa", plant.world_frame(),
    #         "iiwa_link_0", RigidTransform(), plant)

    # weld robot to world frame.
    # plant.WeldFrames(A=plant.world_frame(),
    #                  B=plant.GetFrameByName("iiwa_link_0"),
    #                  X_AB=RigidTransform.Identity())
    plant.Finalize()

    # store reference to all link frames
    link_frames = []
    for i in range(8):
        link_frames.append(plant.GetFrameByName("iiwa_link_%d" % i))

    return plant, link_frames
