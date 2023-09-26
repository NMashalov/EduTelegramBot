# Telegram bot for managment of educational group

Teacher are obedient to accomplish routine tasks of receiving, storing and bringing info in restricted intrefaces

This bot was developed to facilitate that issue for bringing more joy and creativity in educational proccess 

## Active features ✅

### Authorization 👷 
Functional of bot can be restricted with group users
### Tests 📚
Teacher can provide students with simple poll examination
### Task Uploading 🌐
Students can upload their tasks via telegram and can be scheduled to teacher to be estimated and returned with review
### Current results 👨🏻‍🎓 
Student can be provided with essential info about their current progress
### Schedule 📋 
Teacher can remind stundents about lesson start and tasks deadlines  

## Technical start 💥


You can easily start with Docker Compose

If you work with Windows I highly recommend to install WSL2 and then proceed with awesome instruction provided by [Docker docs](https://docs.docker.com/engine/install/ubuntu/) to run docker in linux environment
 
```bash
docker compose up
```

## Modifications 🦾


Technical stack:
- [Aiogram3.0](https://docs.aiogram.dev/en/latest/)
- [SQlAlchemy2.0](https://www.sqlalchemy.org/) for defining ORM model
- [Alembic](https://alembic.sqlalchemy.org/en/latest/tutorial.html) for database migrations

Repository have docs for customizing defined mechanism for your logic 

You can read in depth guide for customization and modification in [docs](docs/docs.md) 
