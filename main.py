import os
import sys
import time
import visualizer

if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

jeff_pipeline = None

def init_model():
    """Loads the Hugging Face safetensors directly into memory."""
    global jeff_pipeline
    if jeff_pipeline is None:
        print("\n⏳ Loading Jeff-Gemma Safetensors into memory (this may take a few moments)...")
        try:
            from transformers import pipeline
            import torch
        except ImportError:
            print("❌ ERROR: Missing dependencies. Please run: pip install transformers torch")
            sys.exit(1)
            
        model_path = "models/Jeff-Gemma4-E2B"
        
        if not os.path.exists(model_path):
            print(f"❌ Error: Model weights not found at {model_path}.")
            print("Please run the 'hf download' command from the README first.")
            sys.exit(1)
            
        device = 0 if torch.cuda.is_available() else -1
        
        try:
            jeff_pipeline = pipeline(
                "zero-shot-classification",
                model=model_path,
                device=device
            )
            print("✅ Model loaded successfully!\n")
        except Exception as e:
            print(f"❌ ERROR: Failed to load real model weights: {e}")
            sys.exit(1)


def query_jeff_model(context_state, candidate_actions):
    """
    Evaluates the state using the local Jeff-Gemma transformer pipeline.
    """
    init_model()
    start_time = time.time()
    
    # Map dictionary to a list of descriptive labels
    labels = list(candidate_actions.values())
    
    # Run real zero-shot classification forward pass
    text_input = f"Screen: {context_state['current_screen']} | Context: {context_state['screen_content']}"
    result = jeff_pipeline(text_input, candidate_labels=labels)
    best_action = result['labels'][0]
    confidence = result['scores'][0]
        
    latency = round((time.time() - start_time) * 1000, 1)
    
    return {
        "action": best_action,
        "confidence": confidence,
        "latency_ms": latency
    }

def run_visual_trajectory():
    print("\n🎨 Generating UI Screenshots in /inputs ...")
    screens = visualizer.generate_svg_screens()
    
    print("🤖 Running Jeff-Gemma decision trajectory over screens...")
    trajectory = []
    
    # Define possible actions for the web UI agent
    actions = {
        "1": "click_login_button",
        "2": "type_admin_username",
        "3": "type_admin_password",
        "4": "wait_for_loading",
        "5": "click_view_reports",
        "6": "scroll_page_down",
        "7": "click_confirm_export",
        "8": "wait_for_export",
        "9": "task_completed_idle"
    }
    
    for filename, title, content in screens:
        context = {
            "current_screen": title,
            "screen_content": content
        }
        
        decision = query_jeff_model(context, actions)
        
        decision['state_id'] = filename
        decision['state_title'] = title
        trajectory.append(decision)
        print(f" -> {title} | Action: {decision['action']} ({decision['latency_ms']}ms)")
        
    print("📈 Building visual dashboard...")
    html_path = visualizer.build_html_dashboard(trajectory)
    print(f"✅ Visual Demo successfully created: {html_path}")

def main():
    print("🧠 Initializing Jeff Gemma AI Brain...")
    run_visual_trajectory()
    
if __name__ == "__main__":
    main()
