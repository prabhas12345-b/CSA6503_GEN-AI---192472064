from sentence_transformers import SentenceTransformer, util
import os

print("Loading resume screening model...")

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

job_description = input(
    "\nEnter engineering job description:\n"
)

resume_folder = "resumes"

resumes = []

for filename in os.listdir(resume_folder):

    if filename.endswith(".txt"):

        path = os.path.join(
            resume_folder,
            filename
        )

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:

            text = file.read()

        resumes.append(
            (filename, text)
        )

job_embedding = model.encode(
    job_description,
    convert_to_tensor=True
)

results = []

for filename, resume in resumes:

    resume_embedding = model.encode(
        resume,
        convert_to_tensor=True
    )

    score = util.cos_sim(
        job_embedding,
        resume_embedding
    ).item()

    results.append(
        (filename, score * 100)
    )

results.sort(
    key=lambda x: x[1],
    reverse=True
)

print("\n==========================================")
print("        RESUME SCREENING RESULTS")
print("==========================================")

for rank, (filename, score) in enumerate(
    results,
    start=1
):

    print(
        f"{rank}. {filename} - {score:.2f}%"
    )
