from aiohttp_healthcheck import HealthCheck
stmt = select(
        [posts, users.c.username]).select_from(j).order_by(posts.c.timestamp)

health = HealthCheck()
health.add_check(check_redis)
health.add_check(check_postgres)
health.add_check(check_webhook)