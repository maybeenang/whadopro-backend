def includeme(config):
    # config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route("home", "/")
    config.add_route("login", "/api/v1/login")
    config.add_route("register", "/api/v1/register")
    config.add_route("logout", "/api/v1/logout")
    config.add_route("project", "/api/v1/project{action:.*}")
    config.add_route("task", "/api/v1/task{action:.*}")
    config.add_route("update_task_status", "/api/v1/update/task")
    config.add_route("project_user_id", "/api/v1/projek{action:.*}")
    config.add_route("member", "/api/v1/member{action:.*}")
