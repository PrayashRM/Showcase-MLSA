import os
import uuid
import json
from datetime import datetime
from typing import Dict, Any

BASE_STORAGE_PATH = "storage/jobs"


class UploadHandler:
    """
    Handles file upload persistence and job creation.
    """

    def __init__(self, base_path: str = BASE_STORAGE_PATH):
        self.base_path = base_path
        os.makedirs(self.base_path, exist_ok=True)

    async def run(self, state: Dict[str, Any]) -> Dict[str, Any]:
        resume_data = state.get("raw_input")
        if not resume_data:
            raise ValueError("No resume data provided")

        job_id = str(uuid.uuid4())
        job_dir = os.path.join(self.base_path, job_id)
        os.makedirs(job_dir, exist_ok=True)

        # Save raw input
        with open(os.path.join(job_dir, "resume.json"), "w") as f:
            json.dump(resume_data, f, indent=2)

        state["job"] = {
            "job_id": job_id,
            "created_at": datetime.utcnow().isoformat(),
            "job_dir": job_dir
        }

        return state
