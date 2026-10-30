# release-state

Which of schryer's repositories the release control plane acts on, in one file,
[`state.json`](state.json). This repository is public, so **don't add a private
repository to that file**: its name would be public too. That would mean making
this repository private first, and a private repository on GitHub Free can't
carry a ruleset.

```json
"some-repo": { "project": "pub", "board": true, "protect": true, "govern": false }
```

| Key | Means |
|---|---|
| `board` | It is graded on the board. |
| `protect` | It carries pubkit's rulesets. The checks they require come from the protect block in its own `pubkit.json`. |
| `govern` | The nightly opens its update pull request. |
| `project` | The group it shows under on the board (optional). |

## Changing it

A change is a pull request, opened by the release app for a signed-in operator
with a note saying why, or by hand by one of schryer's admins. It merges by itself
once `state / valid` passes (`pubkit state --check`). The history of the file is
the record of who changed what, and a revert is another pull request.

Only schryer's admins and the "Sustenaut release state writer" app may write here, so
no collaborators or teams with write access should be added.

## The reader app's values

`pubkit.json` names them, in Bitwarden and on GitHub, and this sends them here:

```sh
./with-secrets ./pubkit app-secrets --check   # checks only, sends nothing
./with-secrets ./pubkit app-secrets
```

The design is the [release control plane](https://claude.ai/artifact/KGAd5vKckHCWbrKQCKMhSV).
