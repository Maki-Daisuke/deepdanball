import os
import sys
import deepdanbooru as dd
import deepdanbooru.project as ddp
import deepdanbooru.data as ddd

CONFIDENT_THRESHOLD = 0.3

project_path = os.environ['PROJECT_PATH']
model = None
tags = None

def init():
    global model, tags
    print(f"Loading model...", end="")
    model = ddp.load_model_from_project(project_path=project_path, compile_model=False)
    print("ok.")
    print(f"Loading tags...", end="")
    tags = ddp.load_tags_from_project(project_path=project_path)
    print("ok.")

def interrogate(image_path) -> list:
    image = ddd.load_image_for_evaluate(
        image_path,
        model.input_shape[2],
        model.input_shape[1]
    )
    image = image.reshape((1, *image.shape[0:3]))
    result = model.predict(image)
    confidents = result[0].tolist()
    tag_list = [(t, c) for t, c in zip(tags, confidents) if c > CONFIDENT_THRESHOLD]
    tag_list.sort(key=lambda x: x[1], reverse=True)
    return [t for (t, _) in tag_list]

def writeToFile(path, text):
    if os.path.exists(path):
        os.rename(path, path + ".bak")
    with open(path, "w") as f:
        f.write(text)

def main():
    init()
    for arg in sys.argv[1:]:
        print(f"Interogating {arg}...")
        tag_list = interrogate(arg)
        print("ok.")
        txt_file = os.path.splitext(arg)[0] + ".txt"
        writeToFile(txt_file, ", ".join(tag_list))
        print(f"Tags written to {txt_file}.")


if __name__ == "__main__":
    main()
