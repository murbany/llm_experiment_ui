import {useEffect, useRef, useState} from "react";

export default function ConversationalAi() {
    const[status, setStatus] = useState<Status>("idle");
    const[inputText, setInputText] = useState("");
    return (
        <div className="flex flex-col h-full max-h-[600px] overflow-y-hidden">
            <ConversationLog messages={['Testing']}/>
            <div className="w-full pb-4 flex px-4">
                <ConversationInput
                    placeholder={getInputPlaceholder(status)}
                    text={inputText}
                    setText={setInputText}
                    // sendMessage={handleSend}
                    disabled={status !== 'idle'}
                />
                <button
                    className="p-2 border rounded bg-gray-100 hover:bg-gray-200 active:bg-gray-300 dark:bg-white dark:text-black font-medium ml-2"
                    // onClick={handleSend}
                >
                    Send
                </button>
            </div>
        </div>
    );

}

type Status = "idle" | "streaming"

function getInputPlaceholder(status: Status){
    switch(status) {
        case "idle":
            return "Ask me anything...";
        case "streaming":
            return "Wait for my response..."
    }
}

interface ConversationLogProps {
    messages: string[];
}

function ConversationLog({messages}: ConversationLogProps) {
    let conversationWindow = useRef<Element | null>(null);

    useEffect(() => {
        if (conversationWindow?.current) {
            conversationWindow.current.scrollTop = conversationWindow.current.scrollHeight;
        }
    }, [messages]);

    return (
        <div
            className="w-full flex-1 overflow-y-auto px-4"
            ref={(el) => (conversationWindow.current = el)}
        >
            {messages.map((message, idx) => (
                <div className="my-4" key={idx}>
                    <div className="text-gray-600 dark:text-gray-200 whitespace-pre-wrap mt-1">
                        {message}
                    </div>
                </div>
            ))}
        </div>
    );
}

interface  ConversationInputProps {
    placeholder: string;
    text: string;
    setText: (text: string) => void;
    // sendMessage: () => void;
    disabled: boolean;
}

function ConversationInput({
   placeholder,
   text,
   setText,
   // sendMessage,
   disabled,
}: ConversationInputProps) {
    return (
        <input
            className="p-2 border rounded w-full block dark:bg-gray-900 dark:text-white"
            type="text"
            placeholder={placeholder}
            value={text}
            disabled={disabled}
            onChange={(e) => setText(e.target.value)}
            onKeyDown={(event) => {
                if (event.key === "Enter" && !event.shiftKey) {
                    event.preventDefault()
                    sendMessage();
                }
            }}
        />
    );
}