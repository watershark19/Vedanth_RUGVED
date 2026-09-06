#Coleman-Liau
mystring="""The digital landscape is shifting at a breathtaking pace, altering how humanity communicates, works, and processes vast repositories of knowledge. Every single day, billions of interconnected devices transmit micro-messages, complex financial spreadsheets, and high-definition multimedia across global networks. This massive influx of data presents both unprecedented opportunities and monumental challenges for modern software engineering. How do we build scalable systems capable of parsing this information without collapsing under the weight of sheer volume? Developers frequently grapple with optimization, algorithmic efficiency, and memory management to ensure seamless user experiences.Consider the intricacies of linguistic analysis. Human language is inherently messy, filled with subtle nuances, idioms, and irregular grammatical frameworks that easily confuse rigid computer programs. When analyzing a block of text, simple software might only count characters or spaces. However, advanced natural language processing requires deep structural comprehension. It must identify the emotional sentiment behind words, distinguish between homonyms, and map syntax tree structures dynamically. Is it truly possible for an artificial entity to grasp the profound depth of human literature? Some skeptics argue that machines merely simulate understanding through statistical probabilities. Proponents, on the other hand, believe we are on the verge of creating genuinely cognitive systems!What does this mean for the future of education and literacy? As automated tools become more prevalent, the way we consume written content changes dramatically. Algorithms now curate our daily news feeds, summarize lengthy academic papers, and even generate creative essays on demand. Consequently, readers must develop strong critical thinking skills to evaluate the validity of machine-generated outputs. We cannot simply rely on automated systems to dictate our understanding of reality. Vigilance is necessary. Education must evolve to emphasize source verification, logical analysis, and ethical reasoning.Ultimately, technology should serve as a powerful amplifier for human capability rather than a total replacement for intellect. By designing robust software today, engineers lay the foundational groundwork for a more informed society tomorrow. The journey ahead is bound to be filled with technical hurdles and philosophical dilemmas. Yet, the pursuit of innovation remains an unstoppable force. Will you join the ranks of those pushing these boundaries, or will you merely watch the future unfold from the sidelines? The choice is entirely yours!"""
total_words=(mystring.split(" "))
total_letters=0
total_sen=0



for char in mystring:
    if char.isalpha():
        total_letters+=1

for symb in mystring:
    if symb=="?" or symb=="!" or symb=="." :
        total_sen+=1

lc=((total_letters)/len(total_words))*100
sc=((total_sen)/len(total_words))*100
grade=0.0588 * lc - 0.296 * sc - 15.8
print(f"The grade level of the text is {grade}")

            