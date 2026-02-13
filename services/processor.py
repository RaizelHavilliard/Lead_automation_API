import pandas as pd
from pathlib import Path
from utils.validator import normalize_email


UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

CLEAN_FILE_PATH = UPLOAD_DIR / "clean_leads.csv"


def process_csv(file_path: Path) -> dict:
    df = pd.read_csv(file_path)

    required_columns = {"name", "email", "company"}
    if not required_columns.issubset(df.columns):
        raise ValueError("CSV must contain name, email, company columns")

    total_leads = len(df)
    invalid_count = 0

    cleaned_rows = []
    seen_emails = set()

    for _, row in df.iterrows():
        name = str(row["name"]).strip()
        email = str(row["email"]).strip()
        company = str(row["company"]).strip()

        try:
            normalized_email = normalize_email(email)
        except ValueError:
            invalid_count += 1
            continue

        if normalized_email in seen_emails:
            continue

        seen_emails.add(normalized_email)

        cleaned_rows.append({
            "name": name,
            "email": normalized_email,
            "company": company
        })

    duplicates_removed = total_leads - invalid_count - len(cleaned_rows)

    clean_df = pd.DataFrame(cleaned_rows)
    clean_df.to_csv(CLEAN_FILE_PATH, index=False)

    return {
        "total_leads": total_leads,
        "duplicates_removed": duplicates_removed,
        "invalid_emails": invalid_count,
        "clean_leads": len(cleaned_rows)
    }
