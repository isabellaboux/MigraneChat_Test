Run with command
```bash
uv run uvicorn main:app --reload
```


# Thoughts
- [ ] Be open for other audio formats - check also what formats whisper is compatible with
- [ ] I noticed some transciption erros (medium -> minimum). We could consider using a larger whisper model:
    - tiny - Smallest, fastest, lowest accuracy (~39MB)
    - base - Current (Currently being used) - Good balance (~140MB)
    - small - Better accuracy, slower (~465MB)
    - medium - Even better accuracy (~1.5GB)
    - large - Best accuracy, slowest (~2.9GB)



#  Steps to deploy this on Google Cloud
Deployment procedure, such tha tthe code gets redeployed at every push. Not 100% sure this is really using docker though.

Step 1: Go to Google Cloud Console
Visit: https://console.cloud.google.com

Step 2: Create/Select a Project
Click the project dropdown (top left)
Create a new project called "MigraineChatAPI"
Wait for it to be created

Step 3: Go to Cloud Run
In the left menu, search for "Cloud Run"
Click on Cloud Run

Step 4: Create Service
Click the blue "Create Service" button
You'll see a form

Step 5: Configure the Service
Fill in:
Service name: migraine-api
Region: us-central1 (or closest to you)
Authentication: Check "Allow unauthenticated invocations"

Step 6: Connect to GitHub
Under "Container image", click "Set up CI/CD" or "Deploy one revision from an existing container image"
Choose "GitHub"
Authenticate with GitHub (login when prompted)
Select your repo: MigraineChatAPI
Branch: main

Step 7: Configure Build
Build type: Select "Dockerfile"
Dockerfile location: Dockerfile (should auto-fill)

Step 8: Set Environment Variables
Scroll down to "Runtime settings" → "Runtime environment variables"
Click "Add variable"
Name: GROQ_API_KEY
Value: YOUR_ACTUAL_API_KEY (paste your Groq API key)

Step 9: Set Memory
Memory: Change to 2 GB (needed for Whisper)

Step 10: Deploy
Click the blue "Deploy" button
Wait 5-10 minutes for build and deployment
You'll get a public URL like: https://migraine-api-xxxxx-uc.a.run.app
That's It!