"""Maintainer software probe; no project implementation or learner artifacts."""

import importlib
import importlib.metadata
import json
import platform
from pathlib import Path
import tempfile
import threading


def main():
    for name in ("flask", "numpy", "pandas", "sklearn.metrics",
                 "sklearn.model_selection", "sklearn.linear_model", "seaborn",
                 "requests", "gunicorn"):
        importlib.import_module(name)

    import matplotlib
    matplotlib.use("Agg")
    from matplotlib import pyplot as plt
    from flask import Flask
    import requests
    from werkzeug.serving import make_server

    with tempfile.TemporaryDirectory(prefix="software-smoke-") as directory:
        target = Path(directory) / "plot.png"
        figure, axes = plt.subplots()
        axes.plot([0, 1], [0, 1])
        figure.savefig(target)
        plt.close(figure)
        assert target.read_bytes().startswith(b"\x89PNG\r\n\x1a\n")

    app = Flask(__name__)
    app.add_url_rule("/health", view_func=lambda: {"status": "ok"})
    server = make_server("127.0.0.1", 0, app)
    worker = threading.Thread(target=server.serve_forever, daemon=True)
    worker.start()
    try:
        response = requests.get(
            f"http://127.0.0.1:{server.server_port}/health", timeout=5
        )
        response.raise_for_status()
        assert response.json() == {"status": "ok"}
    finally:
        server.shutdown()
        worker.join(timeout=5)
        server.server_close()

    versions = {name: importlib.metadata.version(name) for name in
                ("Flask", "numpy", "pandas", "scikit-learn", "matplotlib",
                 "seaborn", "requests", "gunicorn")}
    print(json.dumps({"python": platform.python_version(),
                      "platform": platform.platform(), "packages": versions,
                      "imports": "passed", "headless_plot": "passed",
                      "loopback_http": "passed"}, indent=2))


if __name__ == "__main__":
    main()
