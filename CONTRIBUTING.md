
For contributing you can follow the next steps

first create a new branch.
Use the same number # as the issue in the list

`git checkout -b #_name_of_commit`

Then add the files

`git add .`

(Instead of the . you can also specify the specif file to select)

Next, commit the changes

`git commit -m "concise description of commit"`

And push the commit to Github

`git push origin #_name_of_commit`

This will create an new branch on your remote forked repo.

To send a pull request to the official repo:

- In the project repo, go to "Pull Requests" and choose "Create New Pull Request".
- Click the link to "compare across forks".
- Set your repo as the "head fork", and select the branch that you want to merge.
- Create the pull request, complete with descriptions of changes. If applicable, connect the PR with the issue it addresses.

[GitHub Documentation on creating a pull request from a fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork

)

