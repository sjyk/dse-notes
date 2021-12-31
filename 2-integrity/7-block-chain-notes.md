# Notes on Block Chain and Crypto Currencies
In the last several years, we've seen a rise in "crypto-currencies", or digital data that works as a medium of exchange. These notes help demystify the underlying technologies behind this trend and the essential parts that we (as savy observers of this trend) should understand.

## Motivation
We're going to spend some time understanding exactly what crpyto-currencies are trying to fix. The following is largely my opinion but I think it is a useful way of thinking about it: cryptocurrencies are not about creating a new digital currency but about simplifying the complex trust relationships needed to make currency transactions work. This is hard to digest at first glance but let's see some examples.

### Commodities, Currencies, and Trust
Imagine that you are a farmer living 8000 years ago (before the invention of money), and you need some new seeds for your farm. Your neighbor has exactly the seeds that you want, and you have an extra cow that you would be willing to trade for these seeds. Unfortunately, your neighbor tells you that he has no use for a cow and wants a pig instead. Stuck in this pickle, you would have to search your neighborhood for someone willing to trade a cow for a pig to eventually get the seeds that you need. This is exactly the problem that a "currency" solves: it sets a common medium of exchange that avoids having to organize 3-way, 4-way, or more bartering agreements on your own. You can sell your cow to anyone who needs a cow and receive some units of "currency" in exchange, and use those proceeds to buy seeds. You can now see why the invention of currency revolutionizes economics --- it opens up all sorts of options for buyers and sellers because now you don't have to find someone who is willing to trade a cow for a pig, just someone who is buying a cow. This example is a silly one, and probably historically inaccurate, but it sets up some two key concepts that will be useful later.

* Commodity. A raw material or primary agricultural product that can be bought and sold (e.g., seeds, cows, and pigs)
* Currency. An agreed upon unit of exchange.

The idea of using currency for trade seems great at first glance but there's a crucial piece here that is easy to overlook. Commodities are generally not easily "counterfeitable", you can't make a fake cow. Maybe, one could argue that you can deceptively sell fake seeds, but would eventually reveal themselves to be fake after planting. Compared to the commodities they buy and sell, currency is far easier to fake. Governments today go through great lengths to make it difficult to fake paper currency using serial numbers, metalic strips, special inks, etc. In a sense, this is tradeoff when one moves to an abstract unit of exchange rather than directly bartering over commodities: the more convenient that unit of exchange is (or the more it is divorced from the actualy commodities), the easier it is to fake or forge. 

Thus, traditional currencies only work if we can "trust" the authority that is issuing the currency. It requires all economic participants to trust that there is a system in place to find and identify counterfeit currency, and a system of recourse for unwitting victims. It also requires that they trust that the authority is truthful about the value and amount of currency currently in circulation. All of the issued currency must be accurately accounted for --- untracked currency is basically counterfeit currency. 

So, in today's systems, we place a significant amount of trust, whether we think about it or not, in the systems that issue money and trade in money.
Often times these trust relationships are a couple of steps removed from the customer.
When you write a check and it is cashed by the recepient: it deducts money from your bank account, adds money to the recepients account, that transfer is executed by the banks managing the accounts, proper execution of the transfer is ultimately processed/audited by a hierarchy of governmental and non-governmental financial organizations.
So in the simple cashing of a check, your "money" might actually pass through multiple different parties before it gets to its destination. 
Since there is no physical exchange of currency here, each step along that way needs to be "trusted" so that your money gets to the right place and can be turned into physical currency when you need it.
In a country like the United States, we can take this system of money movement for granted. However, throughout history there have been numerous examples of collapsed currency systems due to government mismanagement or corruption.

### Electronic Currency and Ending the Charade
I noted that in my example above of cashing a check that there is no physical exchange of currency. Eveything that happens when you cash a check happens electronically --- it substracts money from your account in one bank and adds money to the recepient's account. This is a relatively simple task when you think about it, but why do we need the entire aparatus of a banking system to make that work? Again, it comes down to trust. For good reason, you as a private citizen don't have the authority to directly go in to bank accounts that are not yours and add and subtract balances. Your bank acts as a proxy on your behalf (because people trust your bank more) and executes the transfer of funds.

Now, there is an added wrinkle here. Technically speaking, when you put money in a bank, it's becomes the bank's money to lend and invest. And, we don't completely trust banks to always do the right thing. So, all of this money movement happens under the watchful eyes of a central bank, a bank's bank if you will, to make sure that all of the obligations are fulfilled and all transactions are properly executed. 

In this whole system, physical currency is a bit of an afterthought. Nowhere above, do I say that physical dollar bills change hands. In a sense, our modern currency system is *already digital*, where a large number of transactions happen *purely electronically where trustyworthy brokers have to ensure the right additions and subtractions have happened to the right accounts*. Here's the counter-intuitive part...the rise of cryptocurrencies is not about creating a new digital currency (that is already here) but about simplifying the complex trust relationships needed to make such a currency work in reality.

## Engineering A Digital Currency
Our motivating examples show that conducting business with "currency" today requires a complex network of trust relationships: (1) I have faith that the authority issuing the currency is trustworthy, (2) I have faith that all of the currency transactions that I make involve "real" currency, (3) I trust that my bank will properly execute any electronic transactions on my behalf, and (4) we trust that a central banking system acts as an omniscient arbitrer in this whole process. 

Some would argue that this whole system is a bit of an anachronism from a time where electronic money transfer was not realistic -- think big Wells Fargo stage coaches moving money and valuables around the country. At that time, "trust" was literally physical security for these money transfers. Let's now imagine that we fully eliminate all physical currency, and redesign the system from the ground up knowing that all transactions will be done electronically --- could we simplify the trust relationships needed to make it all work?

Let's start by trying to understand what an electronic currency needs to support; the bare minimum features. To make this more concrete, let's call our new electronic currency "widgets" (denoted by Ʊ). 

### Transactions and Ledgers. 
Let's assume we have a database of electronic accounts. Each account has a unique identifier (i.e., an account number), and a total balance of the funds contained therein. Let's say that we can trade in 1000ths of widgets (0.001Ʊ) all the way to 1 billion widgets (1,000,000,000Ʊ). This is what the database would look like:

| Account Number  | Balance | 
|----|----|
| 13241 | 102.001Ʊ | 
| 964682 | 9789.000Ʊ | 
| ... | ... |
| 13317 | 664500.095Ʊ | 

A **transaction** is a transfer of *XƱ* from a *source account* to a *destination account*. The *execution* of a transaction subtracts XƱ from the source account's balance and adds it to the destination account's balance. As an example, consider a transaction
```
Transaction(source=13241, destination=13317, amount=10.000Ʊ)
```
We can execute this transaction over the database and result in:

| Account Number  | Balance | 
|----|----|
| 13241 | 102.001Ʊ - 10.000Ʊ = 92.001Ʊ  | 
| 964682 | 9789.000Ʊ | 
| ... | ... |
| 13317 | 664500.095Ʊ + 10.000Ʊ = 664510.095Ʊ |

At any given time, the *state* of the account database is defined as the balances in every account. Transactions change the state of the account database. If using transactions is the only way one can modify the database, then a *ledger* of all historical transactions is sufficient to determine the state at any point of time. Imagine that we logged all of the transactions all the way from the beginning, we could simply replay history to calculate the state at any time (your account balance). 
This is one way to *audit* the account database. We can easily determine whether the result of replayed transactions match the current account balances that exist in the database. To summarize some key terms that will show up later:

* Transaction. A **transaction** is a transfer of *XƱ* from a *source account* to a *destination account*.
* Ledger. A  **ledger** is a historical log of all transactions in the order in which they occured.
* State. The (global) **state** is the balances in all accounts at any given point in time.
* Audit. An **audit** is a proof that the current global state can be derived from the ledger.

#### Aside for Computer Science Enthusiasts
To a computer, account balance doesn't mean anything. It is simply data stored as 1s/0s in some electronic storage device. How to represent accounts, balances, and transaction (i.e., how to map those real-world concepts down to 1s and 0s) is actually an interesting problrm.
In the example above, there are 1 trillion possible transaction amounts (1000 x 1000000000). We can represent Ʊ as "fixed-point" binary numbers: essentially think of a counter (0 -> 0.001Ʊ, 1->0.002Ʊ,...) that enumerates all of the possible transaction values until (999999999999 -> 1,000,000,000Ʊ). Each one of those counter values represents a possible amount of widgets, and instead of storing those counter values in Base 10 (which is our standard Arabic number system), we store them in Base 2 (binary numbers) on a computer. If we do the math, each transaction amount can be stored in "40 bits" (or 5 bytes) of information. 

This discussion about binary numbers seems completely pedantic but there is a crucial computer science piece here. By default, most computer programs represent decimal numbers in a "floating" point (as opposed to the "fixed point" described above). Let's imagine that you have 1.0Ʊ in your account and you buy something that is worth 0.30Ʊ, you should have 0.7Ʊ remaining in your account. Here's the problem...in a floating point representation there is no guarantee that 0.7Ʊ is stored exactly as such but could be stored as as 0.6999999Ʊ instead. In principle, a malicious user could exploit such issues. Fixed-point arithmetic eliminates such conditions. It enforces that there is a minimum unit of transfer and all possible transaction values are exactly stored. 

### The Centralized Solution and What Goes Wrong
Let's try a first implementation and see what goes wrong. Suppose, that your country has now adopted digital widgets as legal tender. The central bank creates a *central* database of all accounts representing private citizens and businesses. When you go to the store and make a purchase, it immediately triggers a transaction that deducts money from your account and adds money to the businesses account. This transaction is logged in a ledger that can be used to audit the database periodically. 

Let's think about what benefits this centralized solution provides:
1. We've completely eliminated the role of banks (or other intermediaries) as brokers for money transfers between economic participants.
2. There is a unified ledger of ALL transactions (you never have to save a receipt!)
3. The system is independently auditable (anyone can replay the ledger to verify their account balance)

This seems like a reasonable solution, but what could go wrong?
The central database is an authoritative source of all of the money in the system. But, that also makes it a single point of failure. It's kind of like putting "all of your eggs in a single basket". One rogue IT employee could comprimise the database and mess with your account balance. Or, the database could get hacked. Even though the ledger keeps a secondary trail of what's in the database, it doesn't really stop this type of cyber attack. All an attacker needs to do is to create fake transactions that match up with all the changes they make to the database. Or even worse, what if the central bank was politically compromised and just decided to transfer money out of political dissidents' accounts? In short, the centralized, single-database solution is easy to engineer but comes with certain inherent risks.

To fix this problem, we essentially need two pieces:
* A distributed database with multiple replicas of the database state and ledger to avoid a single point of failure.
* A tamper-proof transaction protocol that ensures that only the owner of the account could have generated a transaction originating from his/her account.

These two pieces are solved by a technology called a "block chain". Simply put, it uses cryptography to certify the authenticity of different transactions.

## Block Chain for Dummies
A blockchain is essentially a digital ledger of transactions that is duplicated and distributed across the entire network of computer systems on the blockchain. Each block in the chain contains a number of transactions, and every time a new transaction occurs on the blockchain, a record of that transaction is added to every participant’s ledger. Transactions are recorded with an immutable cryptographic signature.

### Cryptographic Hashes
Let's consider a simple thought experiment. Suppose, we went around the classroom and asked every student to write down a whole number on a strip of paper. We put all of these strips of paper into a bag and give them to one student to keep safe for a week. The next week, we want to confirm that all of the strips of paper are still there (and have their original values!). What if the student lost one of the tickets and made up a value to ensure the count would be the same? Short of writing down every number and putting it in a safe place, how would we efficiently test if some modification happened to the strips of paper (either a lost strip or a manipulated strip)?

Let's consider the following algorithm to test for integrity. When students add their strips of paper to the bag, we incrementally calculate the total value of all of the numbers. When all of the students have added their strips of paper to the bag, we will add the final sum (called a Checksum) on a special colored strip of paper to the bag. When we retrieve the bag next week we simply sum up all of the values again and compare them to the checksum. If the checksum itself is missing then the question is moot as the bag is already untrustworthy.
For example, let's say that we have the following strips of paper:
```
strips = [1,7,4,16,2]
```
The checksum of these strips would be 30 (the sum of all the values). 

It's pretty easy to cheat this checksum. Suppose, you wanted to manipulate the first ticket you could simply add an amount to that ticket and subtract an equivalent amount from another one. 
```
manipulated_strips = [6,7,4,11,2]
```
So, let's make the checksum a little more complicated. What if instead we took the sum of all of the even values, the product of all of the odd values, and then calculated the ratio of the two rouding the value to the nearest integer. Again, looking at our original example:
```
strips = [1,7,4,16,2]
```
The checksum with the new algorithm would be 16. It is a little harder to game this new algorithm by strategically manipulating the numbers. You can convince yourself that if we make this checksum more and more complicated, it will soon become practically impossible to strategically manipulate the data while preserving the original checksum.

A cryptographic hash is a *provably* strong checksum. Essentially, it is a function of data that is very hard to "reverse engineer" (look at the output value and figure out an input that generates it). The intuition is really similar to what we talked about above. Ideally, the only way to find a set of data that produces a given hash is to attempt a brute-force search of possible inputs to see if they produce a match. Basically, it acts as a provable test of data tampering.

How does this relate to our digital currency problem above? Let's re-imagine the transaction protocol described in the centralized solution. Again, let's imagine a scenario where you go to the store and make a purchase. Instead of simply issuing a tranaction to the central database: (1) as before trigger a transaction that deducts money from your account and adds money to the businesses account, (2) you compute a hash value of the entire database after your transaction, and (3) you send copies of that hash value with the accompanying transaction to a collection of third-party auditors. 

This protocol makes it significantly harder to tamper with the database.
Any audit of the database state must not only match up with the ledger but also all of the hash values must match up as well in the third-party databases.
Essentially, it protects the ledger from retroactive modification.
You can't delete or modify historical transactions because then the state of the database will not match up with the hash values in the third party logs.

### The Block Chain
This idea of a hash-based tamper proof ledger is basically the intuition behind the block chain. The block chain is a distributed database where every transaction is logged with a hash verifying the previous database state.
This database is replicated across multiple independent nodes to mitigate failures and attacks on any single node.
If the states of different replicas diverge then a consensus protocol is used to reconcile the differences, e.g., a majority have to agree.
This means that the only way that someone can "tamper" with the database is to control more than a majority of the network.

So, block chains are not all that complicated in the grand scheme of things.
The field of financial accounting has always had similar ideas.
For example, double-entry accounting is a method of bookkeeping that relies on a two-sided accounting entry to maintain financial information. Every entry to an account requires a corresponding and opposite entry to a different account. This is essentially a consensus protocol to detect accounting errors.
Similarly, third-party auditing is performed by an audit organization independent of the customer-supplier relationship and is free of any conflict of interest.
This is similar to the distributed replicas and ledgers that are independent of any single organization's control.
Block chains try to automate these functions at scale and without human supervision --- and it all comes down to a simple cryptographic trick called hashing.

This approach can potentially simplify the financial trust relationships that we talked about earlier.
It has all of the benfits of the centralized solution: (1) it eliminates the need for middle men for money transfer, (2) there is a unified ledger, (3) the system is independently auditable, AND (4) the ledger cannot be retroactively tampered with unless some party "captures" a majority of the database nodes.

#### Aside for Computer Science Enthusiasts
In practice, the block-chain checksums are implemented a little more efficiently. Note, the output of applying a hash function to some data is a checksum. This checksum can be thought of as new data that can further be hashed! In Python notation, here's what we mean:
```
def checksum(data):
	return hash(data)

def checksum2(data):
	return hash(hash(data))
```
Both checksum and checksum2 are valid hash functions of the data. This insight is really useful if we ever wanted to "update" a previously hashed value. Imagine that we had the hash of some dataset, and an update to the dataset. Instead of having to apply the update, and rehash the entire dataset, we can leverage the previous hash value:
```
def checksum(prev_hash, update):
	return hash(concat(prev_hash, update))
```
We can repeatedly apply this algorithm everytime a new update comes along. To verify the hash, we simply have to replay the sequence of updates and ensure that all of the computed hash values line up. If even one of these is wrong, all subsequent ones will likely be wrong as well. Notice that the sequence of transactions t1,t2,t3,..,tN form a "chain" of operations that are applied to the account database. This basic algorithm gives us an efficient hashing scheme that never has to materialize the entire database state to create a verifiable hash of the ledger.


### Authenticated Transactions
A careful reader would have identified a subtle problem with our "tamper-proof" ledger, namely, how do we prove that a transaction was actually issued by you? The hashes only protect the integrity of the ledger after the fact. To fix this problem, we are going to rely on another cryptographic trick.
The basic premise of cyprotography is simple: there are messages (what you want to hide) and there are keys (a sort of password).
We encrypt the message with the key, which returns an encrypted message (called "cipher text") that no one can decipher.
And, you can only decrypt the message (go from cipher text back to the original) if you have the exact key used to encrypt it.

Authentication systems often rely of a special kind of encryption and decryption.
Public-key cryptography, or asymmetric cryptography, is a cryptographic system that uses pairs of keys. Each pair consists of a public key (which may be known to others) and a private key (which may not be known by anyone except the owner). The generation of such key pairs depends on cryptographic algorithms which are based on mathematical problems termed one-way functions. Effective security requires keeping the private key private; the public key can be openly distributed without compromising security.

This is kind of hard to understand so let's think about a real-world analogy.
Private keys are sort of like "keys" (as in your house keys) and public keys are sort of like "locks" (as in the lock on your front door). Everyone, technically speaking, has access to your lock, they can see it, touch it, etc. But, that physical access to the lock is not useful unless you have the key to it; which is only owned by one person. In the same way, public-key cryptography allows you to create cryptographic protocols with "lock-key" relationships.

For example, one can encrypt a message with the public key then only the person with the corresponding private key can decrypt it. This is sort of like slipping a piece of mail into a locked mailbox. The mailbox is completely public (anyone can put mail in it), but onle the person with the key can recieve the mail. Likewise, you can even do the opposite. A person with the private key can encrypt a message and anyone with the public key can decrypt it. This seems kind of backward but it has a really interesting use. Suppose, you encrypt a message that is public knowledge with your private key. The person decrypting it can use your public key to decrypt it -- if the output matches the expected output -- it acts as a proof that you sent the message. Only someone who had the private key could have sent that message.
This "backwards" use of public-key cryptography is sometimes called a "digital signature".

How does this help us with the block chain?
Let's make a modification to our transaction protocol above.
Let's assume that when every account is created you create a public key and private key pair.
You as the account owner have the private key (which you keep safe) and associated with your account is a public key that is public information.
Instead of just sending a hash that authenticates the ledger you now send three things: (1) the hash of the current database state, (2) an encrypted version of the hash using your private key, and (3) an encrpyted version of the hash using the other party's private key.

An auditor replaying the ledger can look at these three values check the following conditions:
* Do the hash values agree with the information in the ledger? (If not the ledger has been tampered with)
* Does the encrypted value (2) decrypt to the provided hash value? (If not the transaction did not originate from you)
* Does the encypted value (3) decrypt to the provided hash value? (If not the recepient did not authorize the transaction)

Adding digital signatures to the block chain gives us all of the properties we had before AND additionally authenticates that the transactions had to be authorized by someone that had access to your private key. Of course, if you lose your private key or share it, it is no longer authenticated.

### Summary
In short, the block chain is a method of creating replicated, tamper-free ledgers. Crypto-currencies are currencies whose transactions are backed and validated by block-chain databases.

## Sustainability Issues and Proof-of-Work
TODO

## Issuing Currency
TODO

