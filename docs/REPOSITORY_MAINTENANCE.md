# Repository Maintenance

## Current `master` State

As checked on 2026-09-02, the public repository
`andreikee/djangocms_akcontact_form` has:

- `master` as its default branch;
- no classic branch-protection rule;
- no repository ruleset;
- pull requests, merge commits, squash merges, and rebase merges enabled.

The repository owner has administrative permission. The current state is a
repository configuration fact, not a recommendation.

## Recommended Protection

Protect `master` with these settings:

1. Require a pull request before merging.
2. Require conversation resolution before merging.
3. Disable force pushes and branch deletion.
4. Enable the option that prevents administrators from bypassing the rules.
5. Require one approval after a second maintainer is available. Until then,
   requiring a pull request with zero approvals is practical for a solo
   maintainer.
6. Require GitHub Actions status checks only after a CI workflow exists and its
   check names are stable.

The protection rule should not require an unavailable status check. The fork
currently has no status checks attached to the reviewed package PR, so adding
required checks before CI exists would block legitimate merges.

## GitHub UI Procedure

Open the repository on GitHub and select **Settings**, **Branches**, and **Add
branch protection rule**. Enter `master`, select the rules above, and save the
rule. The equivalent newer interface is **Settings**, **Rules**, **Rulesets**,
then a branch ruleset targeting `master`.

## Automation Boundary

An administrator can configure the rule through the GitHub REST API or GitHub
CLI. This project does not automate repository-setting changes in the package
code or documentation workflow. Repository protection changes should be made
deliberately by the owner or after explicit authorization, then verified from
the GitHub repository settings and API.