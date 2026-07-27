import subprocess
import sys
from pathlib import Path


def test_cli():
    project_root = Path(__file__).resolve().parent.parent
    src_dir = project_root / "src"
    dictionary = project_root / "data" / "odm.txt"
    work1 = project_root / "data" / "Pan_Tadeusz.txt"
    work2 = project_root / "data" / "Pan_Tedeusz.txt"

    output = project_root / "test_output.txt"
    if output.exists():
        output.unlink()

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "analyzer.cli",
            "--dictionary",
            str(dictionary),
            "--works",
            str(work1),
            str(work2),
            "--output",
            str(output),
            "--dictionary-stats",
            "--no-words",
            "--frequencies",
            "10",
        ],
        cwd=src_dir,
        capture_output=True,
        text=True,
    )

    print(result.stdout)
    print(result.stderr)

    assert result.returncode == 0
    assert output.exists()
    assert output.stat().st_size > 0

    text = output.read_text(encoding="utf-8")
    assert "Dictionary statistics" in text
    assert "Pan_Tadeusz.txt" in text
    assert "Pan_Tedeusz.txt" in text
    assert "TOTAL" in text
    assert "Unknown words" in text
    assert "Top 10 words" in text