# https://github.com/PhilipPartsch/ReConf2023-Product-As-Code/edit/main/docs/requirements/software_specification.rst#L45

from git import Repo


def find_repo(repo_dir):
   repo = Repo(repo_dir, search_parent_directories=True)
   return repo


def get_docu_part_from_path(repo_dir, repo):
   print('type(repo_dir): ' + str(type(repo_dir)))
   from pathlib import Path
   repo_Path = Path(repo.working_dir)
   if repo_dir.is_relative_to(repo_Path):
      return repo_dir.as_posix()[len(repo_Path.as_posix()):]
   else:
      return ''


def get_branch_from_repo(repo):
   branch_name = None
   if not repo.head.is_detached:
      branch_name = repo.head.ref.name
   return branch_name


def get_commit_from_repo(repo):
   commit_name = repo.commit()
   return commit_name


def get_hexsha_from_commit(commit):
   hexsha = commit.hexsha
   return hexsha


def get_base_url_from_repo(repo):
   url = repo.remotes.origin.url
   # the url includes a finishing .git or .git/
   # let's remove them
   remove_from_end =['.git/', '.git']
   for r in remove_from_end:
      if url.endswith(r):
         url = url[:-len(r)]
         break
   splitted_url = url.split('/')
   # try to remove potential git cridentials
   if splitted_url[1] == '': # try to indicate we have a // header
      split_at = splitted_url[2].split('@')
      # remove potential git cridentials by overwritting readed value with value
      if len(split_at) == 2:
         splitted_url[2] = split_at[1]
   url = '/'.join(splitted_url)
   return url


def get_url_from_repo(repo_dir, hoster: str = 'github'):

   commit_url = ''
   if hoster != 'github':
      return commit_url

   try:
      my_repo = find_repo(repo_dir)
      #print('got repo: ' + str(my_repo))
      my_docu_part = get_docu_part_from_path(repo_dir, my_repo)
      #print('got docu part of path: ' + str(my_docu_part))
      my_url = get_base_url_from_repo(my_repo)
      #print('got base url: ' + str(my_url))
      my_branch = get_branch_from_repo(my_repo)
      #print('got branch: ' + str(my_branch))
      my_commit = get_commit_from_repo(my_repo)
      #print('got commit: ' + str(my_commit))
      my_hexsha = get_hexsha_from_commit(my_commit)
      #print('got hexsha: ' + str(my_hexsha))

      if hoster == 'github':
         commit_url = my_url + '/edit/' + my_branch + my_docu_part
   finally:
      return commit_url


def extent_url_with_needs_data(url: str, docname:str = '', doctype: str = '', lineno: None | int = None):
   #docname = 'requirements/software_specification'
   #doctype = '.rst'
   #lineno = 45
   if url.endswith('/'):
      new_url = url
   else:
      new_url = url + '/'
   new_url = new_url + docname + doctype
   if lineno:
      new_url = new_url + '#L' + str(lineno)

   return new_url

def get_github_edit_url_for_need(app, need, needs, *args, **kwargs):
    github_edit_url = app.config.gitlink_edit_url_to_git_hoster
    github_edit_url_for_need = extent_url_with_needs_data(
       url = github_edit_url, 
       docname = need['docname'],
       doctype = need['doctype'],
       lineno = need['lineno']
       )
    return github_edit_url_for_need