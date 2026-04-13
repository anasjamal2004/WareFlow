from app.main import app

# This file serves as the clean entry point for Vercel Serverless Functions.
# By placing it at the root of the "backend" directory (next to requirements.txt),
# Python parses the "app" folder as a proper package, completely eliminating
# the need for sys.path routing hacks.
