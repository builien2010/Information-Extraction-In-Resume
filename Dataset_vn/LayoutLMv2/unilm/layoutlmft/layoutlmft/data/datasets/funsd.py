# coding=utf-8

import json
import os

import datasets

from layoutlmft.data.utils import load_image, normalize_bbox


logger = datasets.logging.get_logger(__name__)


_CITATION = """\
@article{Jaume2019FUNSDAD,
  title={FUNSD: A Dataset for Form Understanding in Noisy Scanned Documents},
  author={Guillaume Jaume and H. K. Ekenel and J. Thiran},
  journal={2019 International Conference on Document Analysis and Recognition Workshops (ICDARW)},
  year={2019},
  volume={2},
  pages={1-6}
}
"""

_DESCRIPTION = """\
https://guillaumejaume.github.io/FUNSD/
"""


class FunsdConfig(datasets.BuilderConfig):
    """BuilderConfig for FUNSD"""

    def __init__(self, **kwargs):
        """BuilderConfig for FUNSD.

        Args:
          **kwargs: keyword arguments forwarded to super.
        """
        super(FunsdConfig, self).__init__(**kwargs)


class Funsd(datasets.GeneratorBasedBuilder):
    """Conll2003 dataset."""

    BUILDER_CONFIGS = [
        FunsdConfig(name="funsd", version=datasets.Version("1.0.0"), description="FUNSD dataset"),
    ]

    def _info(self):
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=datasets.Features(
                {
                    "id": datasets.Value("string"),
                    "tokens": datasets.Sequence(datasets.Value("string")),
                    "bboxes": datasets.Sequence(datasets.Sequence(datasets.Value("int64"))),
                    "ner_tags": datasets.Sequence(
                        datasets.features.ClassLabel(
                            names=["S-AWARDS","S-COMPANY_NAME_REFERENCES", "O","S-POSITION_REFERENCES", "S-PHONE_REFERENCES","S-NAME_REFERENCES", "S-EMAIL_REFERENCES","S-NATION", "S-ADDRESS","S-CERTIFICATE","S-COMPANY_DATE","S-COMPANY_NAME","S-DATE_OF_BIRTH","S-EMAIL","S-GENDER","S-GRADE","S-MAJOR","S-NAME","S-PHONE","S-POSITION","S-SCHOOL_DATE","S-SCHOOL_NAME","S-WEBSITE", "S-PROJECT_NAME"]
                        )
                        # datasets.features.ClassLabel(
                        #     names=["O", "B-HEADER", "I-HEADER", "B-QUESTION", "I-QUESTION", "B-ANSWER", "I-ANSWER"]
                        # )
                    ),
                    "image": datasets.Array3D(shape=(3, 224, 224), dtype="uint8"),
                }
            ),
            supervised_keys=None,
            homepage="https://guillaumejaume.github.io/FUNSD/",
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        """Returns SplitGenerators."""
        #downloaded_file = dl_manager.download_and_extract("https://guillaumejaume.github.io/FUNSD/dataset.zip")
        #filepath = "/content/drive/MyDrive/Lien/Test_layoutlmv2"
        return [
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN, gen_kwargs={"filepath": "/content/drive/MyDrive/CV/CV/Dataset3/LayoutLMv2_Resumes_vn/unilm/layoutlmft/data_vn/training_data/"}
            ),
            datasets.SplitGenerator(
                name=datasets.Split.VALIDATION, gen_kwargs={"filepath": "/content/drive/MyDrive/CV/CV/Dataset3/LayoutLMv2_Resumes_vn/unilm/layoutlmft/data_vn/testing_data/"}
            ),
            datasets.SplitGenerator(
                name=datasets.Split.TEST, gen_kwargs={"filepath": "/content/drive/MyDrive/CV/CV/Dataset3/LayoutLMv2_Resumes_vn/unilm/layoutlmft/data_vn/testing_data/"}
            ),
        ]

    def _generate_examples(self, filepath):
        #filepath = "/content/drive/MyDrive/Lien/Test_layoutlmv2/unilm/layoutlmft/dataset/training_data/"
        logger.info("⏳ Generating examples from = %s", filepath)
        
        ann_dir = os.path.join(filepath, "annotations")
        img_dir = os.path.join(filepath, "images")

        print("\n\nfilepath\n\n", filepath)
        for guid, file in enumerate(sorted(os.listdir(ann_dir))):
            tokens = []
            bboxes = []
            ner_tags = []

            file_path = os.path.join(ann_dir, file)
            with open(file_path, "r", encoding="utf8") as f:
                data = json.load(f)
            image_path = os.path.join(img_dir, file)
            image_path = image_path.replace("json", "jpg")
            image, size = load_image(image_path)
            for item in data["form"]:
                words, label = item["words"], item["label"]
                words = [w for w in words if w["text"].strip() != ""]
                if len(words) == 0:
                    continue
                if label == "other":
                    for w in words:
                        tokens.append(w["text"])
                        ner_tags.append("O")
                        bboxes.append(normalize_bbox(w["box"], size))
                else:
                    tokens.append(words[0]["text"])
                    ner_tags.append("S-" + label.upper())
                    bboxes.append(normalize_bbox(words[0]["box"], size))
                    for w in words[1:]:
                        tokens.append(w["text"])
                        ner_tags.append("S-" + label.upper())
                        bboxes.append(normalize_bbox(w["box"], size))

            yield guid, {"id": str(guid), "tokens": tokens, "bboxes": bboxes, "ner_tags": ner_tags, "image": image}
