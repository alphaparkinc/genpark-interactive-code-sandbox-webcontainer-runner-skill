class InteractiveCodeSandboxWebcontainerRunnerClient:
    def execute_in_sandbox(self, code_files_map: dict, framework: str = "React-TypeScript") -> dict:
        return {
            "live_preview_url": "https://sandbox-runner-8092.webcontainer.app",
            "console_logs": ["HMR update ready", "App mounted successfully"],
            "build_duration_ms": 340
        }
