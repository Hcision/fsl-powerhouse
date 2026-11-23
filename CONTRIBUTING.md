# Contributing

Thanks for helping make this plugin more useful for Salesforce and Field Service teams. Corrections from people who run Field Service in production are the most valuable contributions.

## The one rule

**Every factual statement needs an official Salesforce source.** A reference file states what a page says, when it was read, and links to it. Personal experience is welcome in an issue, and it becomes part of a reference once an official page confirms it. If the documentation is wrong or silent, say so explicitly, as the scheduling reference does under "Documentation inconsistencies seen".

## Ways to contribute

| You want to | Do this |
| --- | --- |
| Fix or add a verified fact | Edit the skill's `reference.md`, add the source link, update the read date |
| Cover a new area | Add `skills/<name>/SKILL.md`, add its row to `knowledge/fsl-topic-map.md`, list it in the README |
| Add a starting point for research | Add an entry to `knowledge/sources.json` with an existing or new topic |
| Report a wrong or outdated statement | Open an issue with the page that contradicts it |

## Writing a skill

- The description says what the skill covers and ends with a sentence starting with "Use when". It contains no colon followed by a space, which would break the frontmatter.
- The body is a short playbook of what to check, in order. Facts go in `reference.md`, not in the playbook.
- Paths use `${CLAUDE_PLUGIN_ROOT}` and `${CLAUDE_SKILL_DIR}`, never relative paths.
- Keep it tool-neutral. Do not assume a specific ticketing, CI or DevOps product.

## Before opening a pull request

```sh
python3 assets/build_banner.py        # only if you added or removed an agent or a skill
python3 -m unittest discover -s tests -v
claude plugin validate . --strict
```

The tests check that every referenced skill, topic, source and file exists, that counts in the README and banner match the repository, and that reference links point to official Salesforce hosts.

## Conduct

Be respectful and assume good intent. Critique statements, not people. Maintainers may edit or remove contributions that are hostile or off topic.
