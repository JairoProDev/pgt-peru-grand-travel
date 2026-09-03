#!/usr/bin/env python3
"""Sync TAREAS-MAESTRO.csv → Google Sheet tab 'Jairo' only."""
from __future__ import annotations

import csv
import sys
from pathlib import Path

SHEET_ID = "1XEeKQGmlTIYmpxJhGceMIgF_Vsn5fLp-kM5UpxXxEPc"
WORKSHEET_NAME = "Jairo"
CREDS = Path(__file__).resolve().parents[2] / ".secrets" / "google-service-account.json"
CSV_PATH = Path(__file__).resolve().parent / "TAREAS-MAESTRO.csv"

SHEET_HEADERS = [
    "fechas",
    "Dia",
    "Track",
    "Epica",
    "Tipo",
    "Tarea",
    "Prioridad",
    "Estado",
    "Fecha Entrega",
    "Link",
    "Evidencia",
    "Metrica",
    "Notas",
]


def load_rows() -> list[list[str]]:
    rows: list[list[str]] = [SHEET_HEADERS]
    with CSV_PATH.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            fi = r.get("fecha_inicio", "")
            ff = r.get("fecha_fin", "")
            fechas = fi if not ff or fi == ff else f"{fi} → {ff}"
            rows.append(
                [
                    fechas,
                    r.get("dia_pgt", ""),
                    r.get("track", ""),
                    r.get("epica_id", ""),
                    r.get("tipo", ""),
                    r.get("tarea", ""),
                    r.get("prioridad", ""),
                    r.get("estado", ""),
                    r.get("fecha_entrega", ""),
                    r.get("link", ""),
                    r.get("evidencia", ""),
                    r.get("metrica", ""),
                    r.get("notas", ""),
                ]
            )
    return rows


def main() -> int:
    if not CSV_PATH.exists():
        print(f"Missing {CSV_PATH}", file=sys.stderr)
        return 1
    if not CREDS.exists():
        print(f"Missing credentials {CREDS}", file=sys.stderr)
        return 1

    try:
        import gspread
        from google.oauth2.service_account import Credentials
    except ImportError:
        print(
            "Run: uv run --with gspread --with google-auth python sync-to-sheets.py",
            file=sys.stderr,
        )
        return 1

    creds = Credentials.from_service_account_file(
        str(CREDS),
        scopes=["https://www.googleapis.com/auth/spreadsheets"],
    )
    gc = gspread.authorize(creds)

    try:
        sh = gc.open_by_key(SHEET_ID)
    except PermissionError:
        print(
            "403: Share spreadsheet with Editor:\n"
            "  pgt-cursor-agent@pgt-integrations.iam.gserviceaccount.com",
            file=sys.stderr,
        )
        return 1

    try:
        ws = sh.worksheet(WORKSHEET_NAME)
    except gspread.WorksheetNotFound:
        ws = sh.add_worksheet(title=WORKSHEET_NAME, rows=500, cols=len(SHEET_HEADERS))

    data = load_rows()
    ws.clear()
    ws.update(data, value_input_option="USER_ENTERED")
    try:
        ws.format("1:1", {"textFormat": {"bold": True}})
    except Exception:
        pass

    print(f"Synced {len(data) - 1} tasks → '{WORKSHEET_NAME}' in '{sh.title}'")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
