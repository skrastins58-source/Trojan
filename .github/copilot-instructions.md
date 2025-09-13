# Trojan Repository Instructions

**CRITICAL**: Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the information documented here.

## Repository Status
This is currently a minimal repository containing only a basic README.md file. There is no build system, dependencies, source code, tests, or CI/CD infrastructure present at this time.

## Working Effectively
Since this repository is in its initial state with minimal content, standard development workflows do not yet apply. The repository currently contains:
- README.md: Basic project title only
- No source code files
- No build configuration
- No package management files
- No testing infrastructure
- No CI/CD workflows

## Current Repository Structure
```
/home/runner/work/Trojan/Trojan/
├── .github/
│   └── copilot-instructions.md
└── README.md
```

### Validated Commands
The following commands have been verified to work in the current repository state:

- `ls -la` - List repository contents
- `cat README.md` - View the README file content
- `git status` - Check repository status
- `git log --oneline` - View commit history

### Commands That Do Not Work
The following commands will fail because the corresponding infrastructure does not exist:
- `npm install` - No package.json exists (Note: may create package-lock.json as side effect)
- `make` - No Makefile exists
- `./configure` - No configure script exists
- Any build commands - No build system configured
- Any test commands - No test infrastructure exists

## Development Guidance
When adding functionality to this repository:

1. **Create appropriate project structure** based on the intended technology stack
2. **Add build configuration** (package.json, Makefile, etc.) as needed
3. **Set up testing infrastructure** before writing significant code
4. **Configure CI/CD workflows** in .github/workflows/ directory
5. **Update these instructions** to reflect new build, test, and run procedures

## Validation
Since there is no functional code to validate:
- No build validation is possible
- No test scenarios exist
- No application functionality to exercise
- Manual validation limited to file system operations and git commands

### Timing and Performance
- All current operations (ls, cat, git status, git log) complete in under 1 second
- No long-running commands exist in the current repository state
- When infrastructure is added, build and test timing information should be documented here with explicit timeout values

### Manual Testing Scenarios
Currently no manual testing scenarios are applicable since:
- No application code exists to exercise
- No build system to validate
- No user interfaces to interact with
- No APIs or services to test

When functional code is added, this section should document specific user scenarios to validate after changes.

## Common Tasks
### Repository root contents
```bash
$ ls -la /home/runner/work/Trojan/Trojan/
total 20
drwxr-xr-x 4 runner runner 4096 Sep 13 03:25 .
drwxr-xr-x 3 runner runner 4096 Sep 13 03:23 ..
drwxrwxr-x 7 runner runner 4096 Sep 13 03:25 .git
drwxrwxr-x 2 runner runner 4096 Sep 13 03:23 .github
-rw-rw-r-- 1 runner runner    8 Sep 13 03:23 README.md
```

### README.md content
```bash
$ cat README.md
# Trojan
```

### Git status
```bash
$ git status
On branch copilot/fix-7
Your branch is up to date with 'origin/copilot/fix-7'.

nothing to commit, working tree clean
```

## Next Steps for Development
When beginning actual development work:

1. **Define project purpose** - Update README.md with project description, goals, and scope
2. **Choose technology stack** - Add appropriate language-specific files (package.json, requirements.txt, etc.)
3. **Create source directory structure** - Organize code files logically
4. **Add build system** - Configure build tools appropriate for chosen technology
5. **Set up testing** - Add test framework and initial test structure
6. **Configure CI/CD** - Add GitHub Actions workflows for automated building and testing
7. **Update these instructions** - Document new build, test, and validation procedures with accurate timing information

### Critical Requirements for Future Updates
When adding functionality that requires build/test commands, these instructions MUST be updated with:
- **Exact command sequences** - Every command must be tested and validated to work
- **Explicit timeout values** - All commands taking >2 minutes need timeout specifications (60+ minutes for builds, 30+ minutes for tests)
- **"NEVER CANCEL" warnings** - Long-running operations must include explicit warnings not to cancel them
- **Manual validation scenarios** - Step-by-step user workflows to validate functionality
- **Dependency installation** - Exact URIs and commands for installing required SDKs and dependencies
- **Failure handling** - Document what to do when commands fail and known workarounds

### Example Format for Future Build Commands
```markdown
## Building the Application
- Install dependencies: `npm install` -- takes 5 minutes. NEVER CANCEL. Set timeout to 10+ minutes.
- Build: `npm run build` -- takes 45 minutes. NEVER CANCEL. Set timeout to 60+ minutes.
- Test: `npm test` -- takes 15 minutes. NEVER CANCEL. Set timeout to 30+ minutes.
```

## Important Notes
- This repository is essentially a blank slate ready for development
- No timing constraints exist for build/test operations since none are configured
- All standard development infrastructure needs to be added
- These instructions should be updated as the project evolves to include specific build commands, timing expectations, and validation procedures

## Comprehensive Command Validation
The following commands have been thoroughly tested and validated:

### Working Commands (✅ Tested)
- `ls -la` - Lists repository contents, completes in <1 second
- `cat README.md` - Shows README content: "# Trojan", completes in <1 second  
- `git status` - Shows git repository status, completes in <1 second
- `git log --oneline` - Shows commit history, completes in <1 second

### Non-Working Commands (❌ Tested and Confirmed to Fail)
- `npm install` - Fails with "ENOENT: no such file or directory, open '/home/runner/work/Trojan/Trojan/package.json'" (Note: creates package-lock.json as side effect if run)
- `make` - Fails with "No targets specified and no makefile found"
- `./configure` - Fails with "No such file or directory"
- Any build commands - No build system configured
- Any test commands - No test infrastructure exists

### Validation Methodology
All commands listed in these instructions have been:
1. Executed in the actual repository environment
2. Verified to produce expected results (success or documented failure)
3. Timed for performance expectations
4. Tested for any side effects (e.g., package-lock.json creation)