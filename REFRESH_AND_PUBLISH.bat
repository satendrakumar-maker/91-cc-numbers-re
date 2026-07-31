@echo off
echo ==========================================
echo  91 CC Numbers (RE) - REFRESH + PUBLISH
echo ==========================================
echo.

cd /d "%~dp0"

REM --- Fix git identity (required for commits) ---
git config user.name "Dashboard Bot" 2>nul
git config user.email "bot@91cc.local" 2>nul

REM --- Fix remote to point to your GitHub repo ---
git remote remove origin 2>nul
git remote add origin https://github.com/satendrakumar-maker/91-cc-numbers-re.git 2>nul

REM Step 1: Download fresh data from Google Sheet
echo [1/4] Downloading fresh data from Google Sheet...
python "%~dp0rebuild_data.py"
if %errorlevel% neq 0 (
    echo ERROR: Data download failed. Check internet connection.
    pause
    exit /b 1
)

REM Step 2: Build dashboard
echo [2/4] Building dashboard HTML...
python "%~dp0build_dashboard.py"
if %errorlevel% neq 0 (
    echo ERROR: Dashboard build failed.
    pause
    exit /b 1
)

REM Step 3: Git commit
echo [3/4] Committing changes...
git add -A
for /f "tokens=2-4 delims=/ " %%a in ('date /t') do (set mydate=%%c-%%a-%%b)
for /f "tokens=1-2 delims=: " %%a in ('time /t') do (set mytime=%%a:%%b)
git commit -m "Auto-update: %mydate% %mytime%" >nul 2>&1
if %errorlevel% neq 0 (
    echo NOTE: No new changes to commit (or commit failed)
)

REM Step 4: Push to GitHub
echo [4/4] Publishing to public URL...
git branch -m main 2>nul
git push -u origin main
if %errorlevel% neq 0 (
    echo.
    echo ==========================================
    echo  PUSH FAILED - Trying alternative method
echo ==========================================
    echo.
    echo If this fails, you may need to:
    echo 1. Sign in to GitHub in your browser first
    echo 2. Or upload files manually on GitHub website
    echo.
    pause
    exit /b 1
)

echo.
echo ==========================================
echo  DONE! Dashboard published!
echo ==========================================
echo.
echo Your public URL (OPEN THIS LINK):
echo https://satendrakumar-maker.github.io/91-cc-numbers-re/dashboard.html?v=%random%
echo.
echo TIP: The ?v=... forces your browser to load the NEW version,
echo      not the old cached one.
echo.
echo Wait 1-2 minutes for GitHub Pages to update, then refresh.
echo.
pause
