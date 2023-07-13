import { useRef } from 'react';


type propType = { textToCopy: string }

const CopyToClipboardButton = ({ textToCopy }: propType) => {
    const buttonRef = useRef(null);

    const copyToClipboard = (_e: any) => {
        navigator.clipboard.writeText(textToCopy).then(() => {
            /* clipboard successfully set */
            const button: any = buttonRef.current;
            button.textContent = "Copied!";
            setTimeout(() => { button.textContent = "Copy to Clipboard"; }, 2000);
        }, () => {
            /* clipboard write failed */
            alert('Failed to copy text to clipboard');
        });
    };

    return (
        <button
            ref={buttonRef}
            onClick={copyToClipboard}
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded w-full">
            Copy
        </button>
    );
}

export default CopyToClipboardButton;
