from client import InteractiveCodeSandboxWebcontainerRunnerClient

def main():
    client = InteractiveCodeSandboxWebcontainerRunnerClient()
    files = {"App.tsx": "export default function App() { return <h1>GenPark AI Sandbox</h1>; }"}
    res = client.execute_in_sandbox(files, "React-TypeScript")
    print(f"Build Duration: {res['build_duration_ms']}ms")
    print(f"Live Preview URL: {res['live_preview_url']}")

if __name__ == "__main__":
    main()
