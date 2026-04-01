import os

c = get_config()

c.JupyterHub.template_paths = ["/srv/jupyterhub/templates"]

c.JupyterHub.authenticator_class = "dummy"
c.Authenticator.admin_users = {"admin"}

c.JupyterHub.spawner_class = "localprocess"
c.LocalProcessSpawner.cmd = ["jupyter-labhub"]

import pwd

_orig_getpwnam = pwd.getpwnam


def _getpwnam_fallback(name):
    try:
        return _orig_getpwnam(name)
    except KeyError:
        return _orig_getpwnam("ubuntu")


pwd.getpwnam = _getpwnam_fallback

c.Spawner.options_form = """
<div id="kubespawner-profiles-list">
  <div class="profile">
    <div class="radio">
      <input type="radio" name="profile" value="base" checked />
    </div>
    <div>
      <h3>Base Environment</h3>
      <p>2 vCPU, 16GB RAM — Standard geospatial data science toolkit</p>
    </div>
  </div>
  <div class="profile">
    <div class="radio">
      <input type="radio" name="profile" value="medium" />
    </div>
    <div>
      <h3>Medium Environment</h3>
      <p>4 vCPU, 32GB RAM — For larger datasets and heavier computations</p>
    </div>
  </div>
  <div class="profile">
    <div class="radio">
      <input type="radio" name="profile" value="power" />
    </div>
    <div>
      <h3>Power Environment</h3>
      <p>8 vCPU, 64GB RAM — High-performance workloads</p>
    </div>
  </div>
</div>
"""

c.Spawner.default_url = "/lab"

c.Spawner.environment.update(
    {
        "JUPYTERHUB_API_URL": "http://127.0.0.1:8081/hub/api",
    }
)

c.JupyterHub.bind_url = "http://0.0.0.0:8000"

c.JupyterHub.cookie_secret_file = "/srv/jupyterhub/data/jupyterhub_cookie_secret"
