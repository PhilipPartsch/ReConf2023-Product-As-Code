# With this scripting we want to generate links to hoster like:
# https://github.com/PhilipPartsch/ReConf2023-Product-As-Code/edit/main/docs/requirements/software_specification.rst#L45
# https://gitlab.com/PhilipPartsch/reconf2023-product-as-code/-/blob/main/docs/requirements/software_specification.rst#L5
# https://gitlab.com/PhilipPartsch/reconf2023-product-as-code/-/blob/requirements/software_specification.rst#L5

from git import Repo
from pathlib import Path
import os

def find_repo(docu_path):
   repo = Repo(docu_path, search_parent_directories=True)
   return repo


def get_repo_path_from_repo(repo):
   repo_Path = Path(repo.working_dir)
   return repo_Path


def get_docu_part_from_repo_path(docu_path, repo_path):
   if docu_path.is_relative_to(repo_path):
      return docu_path.as_posix()[len(repo_path.as_posix()):]
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


def get_hoster_from_url(url):
   split_double_flash = url.split('//', 1)
   hoster_domain: str = ''
   if len(split_double_flash) == 2: # try to indicate we have a // header
      split_flash = split_double_flash[1].split('/', 1)
      hoster_domain = split_flash[0]
      split_dot = hoster_domain.split('.', 1)
      hoster = split_dot[0]
   return hoster


def get_edit_url_from_folder(docu_path, with_docu_part: bool = True, docu_part_default: str = 'docs'):
   commit_url = ''
   try:
      if os.getenv("READTHEDOCS", default = False):
         print('running on readthedocs CI')
         print('got docupath: ' + str(docu_path))
         my_url = os.getenv("READTHEDOCS_GIT_CLONE_URL", default = '')
         remove_from_end =['.git/', '.git']
         for r in remove_from_end:
            if my_url.endswith(r):
               my_url = my_url[:-len(r)]
               break
         print('got base url: ' + str(my_url))
         my_hoster = get_hoster_from_url(my_url)
         print('got hoster: ' + str(my_hoster))
         my_branch = os.getenv("READTHEDOCS_GIT_IDENTIFIER", default = '')
         print('got branch: ' + str(my_branch))
         my_docu_part = os.getenv("DOCS_FOLDER_IN_REPO", default = docu_part_default)
         print('got docu part of path: ' + str(my_docu_part))
      else:
         my_repo = find_repo(docu_path)
         print('got repo: ' + str(my_repo))
         my_url = get_base_url_from_repo(my_repo)
         print('got base url: ' + str(my_url))
         my_hoster = get_hoster_from_url(my_url)
         print('got hoster: ' + str(my_hoster))
         my_branch = get_branch_from_repo(my_repo)
         print('got branch: ' + str(my_branch))
         #my_commit = get_commit_from_repo(my_repo)
         #print('got commit: ' + str(my_commit))
         #my_hexsha = get_hexsha_from_commit(my_commit)
         #print('got hexsha: ' + str(my_hexsha))
         my_repo_path= get_repo_path_from_repo(my_repo)
         print('got repopath: ' + str(my_repo_path))
         my_docu_part = get_docu_part_from_repo_path(docu_path, my_repo_path)
         print('got docu part of path: ' + str(my_docu_part))

      commit_url = my_url
      if my_hoster == 'github':
         commit_url = commit_url + '/edit/'
         if my_branch == None:
            commit_url = commit_url + 'main'
         else:
            commit_url = commit_url + my_branch
         if with_docu_part:
            if not my_docu_part.startswith('/'):
               my_docu_part = '/' + my_docu_part
            commit_url = commit_url + my_docu_part
      elif my_hoster == 'gitlab':
         commit_url = commit_url + '/-/blob/'
         if my_branch == None:
            commit_url = commit_url + 'main'
         else:
            commit_url = commit_url + my_branch
         if with_docu_part:
            if not my_docu_part.startswith('/'):
               my_docu_part = '/' + my_docu_part
            commit_url = commit_url + my_docu_part

   finally:
      return commit_url


def extent_url_with_file(url: str, docname_including_doctype:str = '', lineno: None | int = None):
   # docname_including_doctype = 'requirements/software_specification.rst'
   # lineno = 45
   if url.endswith('/'):
      new_url = url
   else:
      new_url = url + '/'
   new_url = new_url + docname_including_doctype
   if lineno:
      new_url = new_url + '#L' + str(lineno)

   return new_url


def get_githoster_edit_url_for_need(app, need, needs, *args, **kwargs):
   # We could call every time get_edit_url_from_folder, but we have stored it in the conf,
   # to call it only one. 
   github_edit_url = app.config.gitlink_edit_url_to_git_hoster
   github_edit_url_for_need = extent_url_with_file(
      url = github_edit_url, 
      docname_including_doctype = need['docname'] + need['doctype'],
      lineno = need['lineno']
      )
   return github_edit_url_for_need

def get_githoster_edit_url_for_file(file_with_path_inside_docu):
   if file_with_path_inside_docu.isfile():
      path_inside_docu = file_with_path_inside_docu.parent.resolve()
   else:
      path_inside_docu = file_with_path_inside_docu
   github_edit_url = get_edit_url_from_folder(path_inside_docu, with_docu_part = False)
   github_edit_url_for_file = extent_url_with_file(
      url = github_edit_url, 
      docname_including_doctype = file_with_path_inside_docu,
      )
   return github_edit_url_for_file
