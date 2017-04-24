import os


c.JupyterHub.confirm_no_ssl = True
c.JupyterHub.db_url = 'sqlite:////tmp/jupyterhub.sqlite'
c.JupyterHub.cookie_secret_file = '/tmp/jupyterhub_cookie_secret'

# # Do not use any authentication at all - any username / password will work.
c.JupyterHub.authenticator_class = 'ldapauthenticator.LDAPAuthenticator'
c.JupyterHub.spawner_class = 'kubernetes_spawner.KubernetesSpawner'

# ----------------------------------------------------------------------------
# LDAP configuration
# ----------------------------------------------------------------------------

# Example: uid={username},ou=people,dc=wikimedia,dc=org
c.LDAPAuthenticator.bind_dn_template = 'cn={username},cn=jupyterhub,dc=example,dc=org'

## Use SSL to communicate with the LDAP server.
## Defaults True
c.LDAPAuthenticator.use_ssl = False

## Address of the LDAP server to contact. Could be an IP address or hostname.
c.LDAPAuthenticator.server_address = '{{ LDAP_SERVER_IP }}'

## Port on which to contact the LDAP server.
## Defaults to `636` if `use_ssl` is set, `389` otherwise.
#c.LDAPAuthenticator.server_port = '{{ LDAP_SERVER_PORT }}'

# # ----------------------------------------------------------------------------
# # LDAP configuration
# # ----------------------------------------------------------------------------
# Kubernetes namespace to spawn user pods in.
c.KubernetesSpawner.namespace = 'jupyterhub'

c.KubernetesSpawner.verify_ssl = False
c.KubernetesSpawner.hub_ip_from_service = 'jupyterhub'
c.KubernetesSpawner.container_image = 'danielfrg/jupyterhub-kube-ldap-nfs-singleuser:0.1'
c.KubernetesSpawner.persistent_volume_claim_name = 'jupyterhub-volume'
c.KubernetesSpawner.persistent_volume_claim_path = '/mnt'
