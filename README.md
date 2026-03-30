Run with command
```bash
uv run uvicorn main:app --reload
```


# Thoughts
- [ ] Be open for other audio formats - check also if  whisper
- [ ] I noticed some transciption erros (medium -> minimum). We coudl consider using a largfer whisper model:
    - tiny - Smallest, fastest, lowest accuracy (~39MB)
    - base - Current (Currently being used) - Good balance (~140MB)
    - small - Better accuracy, slower (~465MB)
    - medium - Even better accuracy (~1.5GB)
    - large - Best accuracy, slowest (~2.9GB)