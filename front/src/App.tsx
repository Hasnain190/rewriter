import { FormEvent, useState } from "react";

import axios from "axios";
import Loader from "./components/Loader";
import CopyToClipboardButton from "./components/CopyButton";

const App = () => {
  const [isLoading, setIsLoading] = useState(false)
  const [article, setArticle] = useState("")

  const [response, setResponse] = useState("")

  const submitHandler = async (e: FormEvent) => {

    e.preventDefault()

    setIsLoading(true)

    try {
      if (!article) {
        throw Error("Please put something here")
      } if (article.split(" ").length < 900) {
        throw Error(" Article must me at least 1000 words long")

      }
      const config = {
        headers: {

          'Content-type': 'application/json'
        }
      }

      const response = await axios.post(
        '/process', { article }, config

      );

      setResponse(response.data.output);
      setIsLoading(false)
    } catch (error: any) {
      console.error(error);
      setIsLoading(false)
      setResponse(`There is some error  ${error.message}`)
    }


  }

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <h1>Article Rewriter. </h1>
      <p>Rewrite any article from chatgpt</p>
      <div className="max-w-md w-full px-6 py-4 bg-white rounded-lg shadow-md">
        <p className="py-2">Words: {article.split(" ").length}</p>
        <form onSubmit={submitHandler}>
          <textarea
            className="w-full h-32 p-2 mb-4 text-gray-700 border border-gray-300 rounded focus:outline-none focus:border-blue-500"
            placeholder="Write the article for rewrite"
            onChange={e => setArticle(e.target.value)}
          ></textarea>
          <button className="px-4 py-2 bg-blue-500 text-white rounded focus:outline-none">
            Rewrite
          </button>

        </form>
      </div>
      <div className="max-w-md w-full px-6 py-4 bg-white rounded-lg shadow-md">
        <p className="py-2 w-full">Words: {response.split(" ").length}</p>
        {response && <CopyToClipboardButton textToCopy={response} />}
        {isLoading ? <Loader /> :
          <pre className="whitespace-pre-wrap overflow-auto">
            {response}
          </pre>
        }
      </div>
    </div>
  );
};

export default App;
