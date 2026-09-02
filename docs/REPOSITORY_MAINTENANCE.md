# Repository Maintenance

## Current `master` State

As checked on 2026-09-02, the public repository
`andreikee/djangocms_akcontact_form` has:

- `master` as its default branch;
- an active classic branch-protection rule;
- no repository ruleset;
- pull requests, merge commits, squash merges, and rebase merges enabled.

The active rule requires pull requests, resolves conversations before merge,
enforces the rules for administrators, disables force pushes and branch
deletion, and requires zero approvals. No status check is required yet because
the repository has no stable CI workflow.

The repository owner has administrative permission. The current state is a
repository configuration fact, not a recommendation.

## Applied Protection Policy

The current `master` protection uses these settings:

1. Require a pull request before merging.
2. Require conversation resolution before merging.
3. Disable force pushes and branch deletion.
4. Enable the option that prevents administrators from bypassing the rules.
5. Require one approval after a second maintainer is available. Until then,
   requiring a pull request with zero approvals is practical for a solo
   maintainer.
6. Require GitHub Actions status checks only after a CI workflow exists and its
   check names are stable.

The rule intentionally does not require an unavailable status check. Once a
stable CI workflow exists, required checks can be added deliberately.

## GitHub UI Procedure

Open the repository on GitHub and select **Settings**, **Branches**, and **Add
branch protection rule**. Enter `master`, select the rules above, and save the
rule. The equivalent newer interface is **Settings**, **Rules**, **Rulesets**,
then a branch ruleset targeting `master`.

## Automation Boundary

An administrator can configure the rule through the GitHub REST API or GitHub
CLI. The current rule was applied through the GitHub REST API after explicit
owner authorization and verified through the API. Future repository-setting
changes should be made deliberately and verified from GitHub settings and API.